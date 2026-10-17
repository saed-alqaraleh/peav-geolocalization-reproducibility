# Reproducing the numerical findings

## Inputs

The two compressed tables under `data/derived/` represent 3,331 physical queries and 13,324 paired retriever–matcher records. Every query must have exactly four configuration rows. These are **already computed model outputs**, not raw images or raw local-feature caches.

## Commands

```bash
python -m pip install -r requirements.txt
python scripts/reproduce_all.py
python -m pytest -q
```

For a 10,000-replicate Monte Carlo confidence interval consistency check (not identical RNG streams to the frozen 100,000-replicate runs):

```bash
python scripts/replay_primary.py --bootstrap 10000
```

## Assertions

- Query/cell uniqueness, counts, grouping, matched four-configuration consistency.
- Per-dataset Recall@1 and mean verification depth for ten policies, and six-way equal-weight pooling.
- Four protected headline contrasts against the frozen verdict and stored point estimates.
- The 18 depth-by-evidence-state protected discrimination metrics rederived from frozen per-cell scores.
- Frozen development/external operating-point comparison and four configuration-level direction/interval flags.
- Frozen noninferiority and label-access protocol records.

## Frozen inference

The original primary 95% intervals derive from 100,000 resamples stratified by dataset and clustered by physical query, using seed 20260926. The stored interval file is authoritative. In this release, the optional replay produces a statistically consistent independent Monte Carlo estimate but is not claimed to duplicate its exact original random-number sequence.

## Non-goals

This is a reproducible numerical evaluation archive. It does not automatically download protected images, retrain stopping models, rerun matching, reconstruct original intermediate scores, or regenerate manuscript figures. Those operations require separately controlled model/dataset artifacts and the full historical execution environment.
