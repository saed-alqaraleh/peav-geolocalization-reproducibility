#!/usr/bin/env python3
"""Replay PEAV protected point estimates using frozen physical-query aggregates.

Not an end-to-end re-execution of retrieval/matching/model fitting.
"""
from pathlib import Path
import argparse
import numpy as np
import pandas as pd
import json

ROOT = Path(__file__).resolve().parents[1]
QUERY = ROOT/'data/derived/PROTECTED_QUERY_RESULTS.csv.gz'
CELL = ROOT/'data/derived/PROTECTED_CELL_RESULTS.csv.gz'
SUMMARY = ROOT/'results/primary/PROTECTED_DATASET_SUMMARY.csv'
VERDICT = ROOT/'results/primary/FINAL_PROTECTED_VERDICT.json'
BOOT = ROOT/'results/primary/PROTECTED_BOOTSTRAP_CONTRASTS.csv'
METHODS = ['fixed_m5','fixed_m10','fixed_m20','fixed_m30','fixed_m50','fixed_m100','retrieval_scheduler','one_shot_inlier_gate','progressive_inlier_only','full_peav']
N = {'msls':740, 'tokyo247':147, 'gardens-point':200, 'spedtest':607, 'amstertime':1231, '17-places':406}

def replay(check=True):
    q = pd.read_csv(QUERY)
    cell = pd.read_csv(CELL)
    assert q.shape[0] == 3331 and cell.shape[0] == 13324
    assert not q.duplicated(['dataset','query_id']).any()
    assert not cell.duplicated(['dataset','query_id','retriever_key','backend']).any()
    counts=cell.groupby(['dataset','query_id']).size()
    assert counts.eq(4).all(), 'not exactly four cells per physical query'
    assert q.groupby('dataset').size().to_dict()==N
    assert set(q[['dataset','query_id']].itertuples(index=False,name=None))==set(counts.index.tolist())
    assert cell[['retriever_key','backend']].drop_duplicates().shape[0]==4
    merged=q.set_index(['dataset','query_id'])
    # Verify query-level outputs really average all four retriever×backend cells.
    for meth in METHODS:
        for key in ['correct','m']:
            col=f'{key}__{meth}'
            reconstructed=cell.groupby(['dataset','query_id'])[col].mean().reindex(merged.index)
            assert np.allclose(reconstructed.to_numpy(),merged[col].to_numpy(),rtol=0,atol=1e-12),f'cell-query mismatch {col}'
    old=pd.read_csv(SUMMARY).sort_values(['dataset','method']).reset_index(drop=True)
    rows=[]
    for ds,g in q.groupby('dataset'):
        for meth in METHODS:
            rows.append(dict(dataset=ds,method=meth,recall_at_1=g[f'correct__{meth}'].mean(),mean_m=g[f'm__{meth}'].mean(),physical_queries=len(g)))
    new=pd.DataFrame(rows).sort_values(['dataset','method']).reset_index(drop=True)
    assert old[['dataset','method','physical_queries']].equals(new[['dataset','method','physical_queries']])
    for c in ['recall_at_1','mean_m']:
        assert np.allclose(new[c],old[c],atol=1e-12,rtol=0),f'dataset summary mismatch: {c}'
    sums=new.groupby('method')[['recall_at_1','mean_m']].mean()
    v=json.loads(VERDICT.read_text())
    checks={'equal_dataset_full_recall':sums.loc['full_peav','recall_at_1'],
        'equal_dataset_m50_recall':sums.loc['fixed_m50','recall_at_1'],
        'equal_dataset_comparator_recall':sums.loc['progressive_inlier_only','recall_at_1'],
        'equal_dataset_full_mean_m':sums.loc['full_peav','mean_m'],
        'equal_dataset_comparator_mean_m':sums.loc['progressive_inlier_only','mean_m']}
    for k,x in checks.items():assert np.isclose(float(x),v[k],rtol=0,atol=1e-12),(k,x,v[k])
    contrasts={
       'Recall full - fixed_m50':checks['equal_dataset_full_recall']-checks['equal_dataset_m50_recall'],
       'Recall full - progressive_inlier_only':checks['equal_dataset_full_recall']-checks['equal_dataset_comparator_recall'],
       'Mean depth full - progressive_inlier_only':checks['equal_dataset_full_mean_m']-checks['equal_dataset_comparator_mean_m'],
       'Mean depth full - fixed_m50':checks['equal_dataset_full_mean_m']-50.0}
    ref=pd.read_csv(BOOT)
    for _,r in ref.iterrows():assert np.isclose(contrasts[r['contrast']],r['point'],atol=1e-12,rtol=0)
    if check:print('PASS: 3,331 physical queries; 13,324 cells; four per query; six datasets; all method summaries; frozen verdict; four contrast point estimates')
    for k,x in checks.items():print(f'{k}: {x:.12f}')
    for k,x in contrasts.items():print(f'{k}: {x:.12f}')
    return q, checks, contrasts

def bootstrap(q,B=10000,seed=20260926,chunk=512):
    """Re-sample physical queries within dataset, keeping pre-averaged four-cell values together.

    A Monte Carlo consistency check, not a promise of exact replicate identity with the
    canonical 100k archived bootstrap (RNG order/algorithm need not coincide).
    """
    rng=np.random.default_rng(seed)
    ordered=['Recall full - fixed_m50','Recall full - progressive_inlier_only',
        'Mean depth full - progressive_inlier_only','Mean depth full - fixed_m50']
    ds=[]
    for name,group in q.groupby('dataset'):
        vec=np.stack([group['correct__full_peav'].to_numpy()-group['correct__fixed_m50'].to_numpy(),
           group['correct__full_peav'].to_numpy()-group['correct__progressive_inlier_only'].to_numpy(),
           group['m__full_peav'].to_numpy()-group['m__progressive_inlier_only'].to_numpy(),
           group['m__full_peav'].to_numpy()-group['m__fixed_m50'].to_numpy()],axis=1)
        ds.append(vec)
    allb=np.empty((B,4),dtype=float)
    for start in range(0,B,chunk):
        b=min(chunk,B-start)
        agg=np.zeros((b,4),dtype=float)
        for vec in ds:
            picks=rng.integers(0,len(vec),size=(b,len(vec)))
            agg+=vec[picks].mean(axis=1)/len(ds)
        allb[start:start+b]=agg
    ci=np.quantile(allb,[.025,.975],axis=0)
    for j,name in enumerate(ordered):print(f'{name}: Monte Carlo CI [{ci[0,j]:.10f}, {ci[1,j]:.10f}]')
    return ci

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');p.add_argument('--bootstrap',type=int,default=0)
    args=p.parse_args()
    q,*_=replay(True)
    if args.bootstrap:bootstrap(q,args.bootstrap)
