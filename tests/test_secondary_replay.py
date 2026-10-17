import importlib.util
from pathlib import Path

def _run(name):
    p=Path(__file__).resolve().parents[1]/'scripts'/name
    spec=importlib.util.spec_from_file_location(name.replace('.py',''),p)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod.run()

def test_evidence_ladder():
    assert len(_run('replay_evidence_ladder.py'))==18

def test_transfer_curves():
    assert len(_run('check_transfer_curves.py'))==2
