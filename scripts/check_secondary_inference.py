#!/usr/bin/env python3
"""Validate the reported four-cell inference flags without changing any estimates."""
import pandas as pd
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def run():
    df=pd.read_csv(ROOT/'results/secondary/ADDENDUM_E12_INFERENCE_FLAGS.csv')
    assert len(df)==4 and set(df.retriever)=={'cosplace','r2former'} and set(df.backend)=={'disk','aliked'}
    assert (df.physical_queries==3331).all()
    negative=(df.delta_recall_full_minus_inlier<0)
    assert negative.sum()==4
    supported=(df.delta_recall_ci95_high<0)
    assert supported.sum()==3
    nonsig=df.loc[~supported, ['retriever','backend']]
    assert nonsig.to_dict('records')==[{'retriever':'cosplace','backend':'disk'}]
    assert (df['negative_recall_ci_excludes_zero']==supported).all()
    print('PASS: four negative point effects; three confidence intervals below zero; CosPlace-DISK interval crosses zero')
    return df
if __name__=='__main__':run()
