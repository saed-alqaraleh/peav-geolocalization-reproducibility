# PEAV: Reproducible Evaluation for Visual Geolocalization

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23437658.svg)](https://doi.org/10.5281/zenodo.23437658)

Executable numerical evaluation, frozen experimental settings, and derived evidence for **progressive evidence-aware verification (PEAV)** under cross-environment transfer.

This repository provides a self-contained, CPU-based replay of the frozen evaluation results. No pretrained models, GPUs, external datasets, or API keys are needed for the included verification tasks.

## Quick start

```bash
git clone https://github.com/saed-alqaraleh/peav-geolocalization-reproducibility.git
cd peav-geolocalization-reproducibility
python -m pip install -r requirements.txt
python scripts/reproduce_all.py
python scripts/verify_checksums.py
python -m pytest -q
```

The replay validates Recall@1, per-query matching expenditure, physical-query aggregation, all four policy contrasts, evidence-ladder statistics, and frozen development-to-protected operating points. The GitHub Actions workflow runs the same checks on each push.

## Evidence and evaluation

The protected evaluation includes **3,331 physical queries** from six datasets with **13,324** retriever–matching-backend cells: two global retrieval branches (CosPlace and R2Former) and two local matchers (DISK–LightGlue and ALIKED–LightGlue with MAGSAC++ verification). The primary aggregation is the unweighted mean of six dataset-level quantities; the four cells belonging to one physical query are treated as matched observations.

| Frozen policy | Equal-dataset Recall@1 | Mean verified candidates |
| --- | ---: | ---: |
| Fixed depth, m=50 | 62.25% | 50.00 |
| Progressive inlier-only | 60.80% | 19.29 |
| Full PEAV | 59.64% | 21.27 |

The original noninferiority assessment used a margin of 0.5 percentage points relative to fixed 50-candidate verification. Full PEAV did not meet that criterion on the external protected suite. Post-evaluation analyses are retained as **descriptive** evidence of how verification policies transfer; they do not replace the frozen test.

## Repository contents

| Directory | Contents |
| --- | --- |
| [`scripts/`](scripts/) | Reconstruct primary metrics, evidence ladder, transfer curves and configuration contrasts |
| [`tests/`](tests/) | Automated structural, numerical, protocol, and file-integrity checks |
| [`data/derived/`](data/derived/) | Frozen matched per-query and per-configuration outputs |
| [`results/primary/`](results/primary/) | Prespecified protected results and archived confidence intervals |
| [`results/secondary/`](results/secondary/) | Clearly labeled post-evaluation transfer diagnostics |
| [`configs/`](configs/) | Frozen decisions and analysis specifications |
| [`docs/`](docs/) | Reproduction instructions, dataset conventions and evidence provenance |
| [`manifests/`](manifests/) | Authoritative archive hashes and protocol integrity evidence |

## Scope of reproduction

The accompanying code **replays numerical evaluation from frozen derived outputs** and verifies its correspondence with the archived primary summaries. It does not rerun image retrieval, neural feature extraction, geometric matching, or controller training from original images. Those upstream stages require separately licensed benchmark images, original matching caches, and fitted controller artifacts. The numerical replay needs none of them.

The archived 100,000-replicate clustered bootstrap intervals are supplied with the primary results. An independent lower-replicate consistency check does not imply byte-for-byte reconstruction of the original draws.

The repository does not include manuscript text, article figures, original benchmark imagery, private project notebooks, or third-party pretrained weights. Dataset protocols and source attribution are described in [`docs/DATASETS.md`](docs/DATASETS.md) and [`docs/THIRD_PARTY_RESOURCES.md`](docs/THIRD_PARTY_RESOURCES.md).

## Verification and provenance

Run `python scripts/verify_checksums.py` to check the published evidence against [`SHA256SUMS`](SHA256SUMS). Frozen protocol and archive provenance are recorded in [`docs/PROVENANCE.md`](docs/PROVENANCE.md). Reproduction details are in [`docs/REPRODUCE.md`](docs/REPRODUCE.md).

The package is associated with research on the transferability of adaptive verification in visual geolocalization. Please credit the original benchmark and software providers listed in the resource documentation.

## Archival citation

Version **v1.0.0** of this reproducibility package is archived on Zenodo: [10.5281/zenodo.23437658](https://doi.org/10.5281/zenodo.23437658). This DOI identifies the frozen software and derived evaluation resources for the release; the present repository provides the maintained source and numerical replay instructions.
