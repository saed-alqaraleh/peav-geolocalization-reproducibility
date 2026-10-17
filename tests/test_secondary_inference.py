import importlib.util
from pathlib import Path

def test_e12_flags():
    p=Path(__file__).resolve().parents[1]/'scripts/check_secondary_inference.py'
    s=importlib.util.spec_from_file_location('check_e12',p)
    m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
    assert len(m.run())==4
