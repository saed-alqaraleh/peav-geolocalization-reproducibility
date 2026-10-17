import json,hashlib
from pathlib import Path

def test_label_access_and_backend_freeze():
    root=Path(__file__).resolve().parents[1]
    g=json.loads((root/'manifests/PROTECTED_ACCESS_AND_WORKER_GATE_SUMMARY.json').read_text())
    assert g['protected_label_gate_before_open']['protected_labels_opened'] is False
    assert g['protected_label_gate_before_open']['no_protected_retuning'] is True
    assert g['post_freeze_label_open']['protected_retuning_performed'] is False
    assert g['post_freeze_label_open']['candidate_rows_in_source']==1332400
    freeze_hash=hashlib.sha256((root/'configs/PHASE1E_FINAL_DEV_FREEZE.json').read_bytes()).hexdigest()
    assert freeze_hash==g['protected_label_gate_before_open']['phase1e_freeze_sha256']
    assert sum(b['retriever_backend_cells'] for b in g['backends'].values())==13324
