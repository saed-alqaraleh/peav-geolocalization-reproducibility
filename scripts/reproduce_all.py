#!/usr/bin/env python3
"""One-command PEAV frozen-numerical-replay entry point."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMMANDS = (
    'replay_primary.py',
    'replay_evidence_ladder.py',
    'check_transfer_curves.py',
    'check_secondary_inference.py',
)

def main() -> int:
    for name in COMMANDS:
        print(f"\n===== {name} =====", flush=True)
        proc = subprocess.run([sys.executable, str(ROOT / 'scripts' / name)], cwd=ROOT, check=False)
        if proc.returncode:
            print(f"FAILED: {name} (exit {proc.returncode})", file=sys.stderr)
            return proc.returncode
    print("\nPASS: PEAV frozen numerical-reproduction checks completed.")
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
