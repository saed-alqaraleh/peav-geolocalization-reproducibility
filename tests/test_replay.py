import importlib.util
from pathlib import Path

def test_primary():
    p=Path(__file__).resolve().parents[1]/'scripts/replay_primary.py'
    spec=importlib.util.spec_from_file_location('replay_primary',str(p))
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    df, checks, contrasts=mod.replay(check=False)
    assert len(df)==3331
    assert round(checks['equal_dataset_full_recall'],6)==0.596412
    assert round(checks['equal_dataset_comparator_recall'],6)==0.608025
    assert contrasts['Recall full - fixed_m50']<0
    assert contrasts['Mean depth full - progressive_inlier_only']>0
