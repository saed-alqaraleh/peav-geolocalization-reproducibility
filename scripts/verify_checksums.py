#!/usr/bin/env python3
"""Verify the file inventory as packaged, without network access."""
from pathlib import Path
import hashlib

ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'SHA256SUMS'

def main():
    entries=[line.split('  ',1) for line in MANIFEST.read_text().splitlines() if line.strip()]
    for digest,relative in entries:
        path=ROOT/relative
        if not path.is_file():
            raise SystemExit(f'Missing file: {relative}')
        actual=hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != actual:
            raise SystemExit(f'Hash mismatch: {relative}')
    print(f'PASS: {len(entries)} recorded file SHA-256 digests match')

if __name__ == '__main__':
    main()
