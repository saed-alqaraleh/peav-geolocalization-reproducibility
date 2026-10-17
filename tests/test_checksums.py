import importlib.util
from pathlib import Path

def test_checksums():
    root=Path(__file__).resolve().parents[1]
    spec=importlib.util.spec_from_file_location('verify',root/'scripts/verify_checksums.py')
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.main()
