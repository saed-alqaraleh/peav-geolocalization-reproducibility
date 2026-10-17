#!/usr/bin/env python3
"""Independently recompute the protected evidence ladder from released frozen cell outputs.

Continuation-gain target at depth m: an incorrect fixed-m prediction that becomes
correct under the fixed-m50 reference. The score is a higher-is-more-likely gain
probability and each physical query remains represented by four matched cells.
These are diagnostic cell-level discrimination metrics, NOT primary inference CIs.
"""
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.metrics import average_precision_score, roc_auc_score
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data/derived/PROTECTED_CELL_RESULTS.csv.gz'
EXPECTED=ROOT/'results/primary/PROTECTED_EVIDENCE_LADDER.csv'
STATES=('G','I','G+I','G+L','G+L+S','G+L+S+A')
def run():
    data=pd.read_csv(DATA); expected=pd.read_csv(EXPECTED)
    assert len(data)==13324 and len(expected)==18
    rows=[]
    for depth in (5,10,20):
        y=((data['correct__fixed_m50'].to_numpy()>0.5)&(data[f'correct__fixed_m{depth}'].to_numpy()<0.5)).astype(int)
        for state in STATES:
            s=data[f'p__{state}__m{depth}'].to_numpy(float)
            rows.append({'depth':depth,'state':state,'n':len(y),'positives':int(y.sum()),
                         'AUPRC':average_precision_score(y,s),'AUROC':roc_auc_score(y,s)})
    actual=pd.DataFrame(rows)
    merged=actual.merge(expected,on=['depth','state'],suffixes=('_calc','_archive'),validate='one_to_one')
    assert len(merged)==18
    for name in ('n','positives','AUPRC','AUROC'):
        a=merged[f'{name}_calc'].to_numpy(float);b=merged[f'{name}_archive'].to_numpy(float)
        assert np.allclose(a,b,atol=1e-12,rtol=0),f'mismatch: {name} max={abs(a-b).max()}'
    for depth in (5,10,20):
        rows=actual[actual.depth.eq(depth)].set_index('state')
        print(f"m={depth}: inlier AUPRC={rows.loc['I','AUPRC']:.6f}, full AUPRC={rows.loc['G+L+S+A','AUPRC']:.6f}, "
              f"inlier AUROC={rows.loc['I','AUROC']:.6f}, full AUROC={rows.loc['G+L+S+A','AUROC']:.6f}")
    print('PASS: all 18 evidence-state rows exactly reproduce AUPRC, AUROC and gain prevalence')
    return actual
if __name__=='__main__':run()
