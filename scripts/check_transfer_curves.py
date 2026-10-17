#!/usr/bin/env python3
"""Verify frozen threshold points in development and protected descriptive curves.

The sweeps are post-hoc descriptive and MUST NOT be used to retune the protected suite.
"""
from pathlib import Path
import json
import pandas as pd
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
DEV=ROOT/'results/secondary/DEVELOPMENT_ACCURACY_COMPUTE_CURVES.csv'
EXT=ROOT/'results/secondary/POSTHOC_PROTECTED_ACCURACY_COMPUTE_CURVES.csv'
FREEZE=ROOT/'configs/PHASE1E_FINAL_DEV_FREEZE.json'
RESULTS=ROOT/'results/primary/FINAL_PROTECTED_VERDICT.json'
def run():
    freeze=json.loads(FREEZE.read_text()); verdict=json.loads(RESULTS.read_text())
    out={}
    for name,file in [('development_5400',DEV),('protected',EXT)]:
        df=pd.read_csv(file)
        assert len(df)==404 and set(df['method'])=={'full_peav','progressive_inlier_only'}
        assert set(df.stage)=={name} and df.is_frozen_threshold.sum()==2
        frozen=df[df.is_frozen_threshold].set_index('method')
        assert set(frozen.index)=={'full_peav','progressive_inlier_only'}
        out[name]=frozen
        for method,row in frozen.iterrows():
            print(f"{name} {method}: recall={row['recall_at_1']:.8f}, mean_m={row['mean_m']:.8f}, threshold={row['threshold']:.9f}")
    # Canonical protected values are stored as equal-dataset weighted summary.
    assert np.isclose(out['protected'].loc['full_peav','recall_at_1'],verdict['equal_dataset_full_recall'],atol=1e-11,rtol=0)
    assert np.isclose(out['protected'].loc['progressive_inlier_only','recall_at_1'],verdict['equal_dataset_comparator_recall'],atol=1e-11,rtol=0)
    assert np.isclose(out['protected'].loc['full_peav','mean_m'],verdict['equal_dataset_full_mean_m'],atol=1e-11,rtol=0)
    assert np.isclose(out['protected'].loc['progressive_inlier_only','mean_m'],verdict['equal_dataset_comparator_mean_m'],atol=1e-11,rtol=0)
    for method in ['full_peav','progressive_inlier_only']:
        assert np.isclose(out['development_5400'].loc[method,'threshold'],out['protected'].loc[method,'threshold'],atol=1e-14,rtol=0)
    assert out['development_5400'].loc['full_peav','recall_at_1']>out['development_5400'].loc['progressive_inlier_only','recall_at_1']
    assert out['protected'].loc['full_peav','recall_at_1']<out['protected'].loc['progressive_inlier_only','recall_at_1']
    print('PASS: frozen-threshold operating points and descriptive stage-reversal checks')
    return out
if __name__=='__main__':run()
