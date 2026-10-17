from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def test_figures_and_manuscript_not_redistributed():
    assert not list(ROOT.rglob('*.pdf'))
    assert not list(ROOT.rglob('*.tex'))
    assert not list(ROOT.rglob('*.ipynb'))
    assert not list(ROOT.rglob('*.png'))
    assert not list(ROOT.rglob('*.jpg'))

def test_frozen_outputs_exist():
    assert (ROOT/'data/derived/PROTECTED_QUERY_RESULTS.csv.gz').is_file()
    assert (ROOT/'data/derived/PROTECTED_CELL_RESULTS.csv.gz').is_file()
    assert (ROOT/'configs/PHASE1E_FINAL_DEV_FREEZE.json').is_file()
