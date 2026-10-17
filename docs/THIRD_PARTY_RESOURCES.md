# Upstream methods and dataset resources

The reference implementation used separately licensed, independently developed retrieval and image-matching methods. This repository does not bundle their upstream source code, model weights or photographs.

- [CosPlace](https://github.com/gmberton/CosPlace) — a global descriptor retrieval method.
- [R2Former](https://github.com/bytedance/R2Former) — a place-recognition retrieval and reranking framework. The PEAV study uses its global retrieval branch.
- [LightGlue](https://github.com/cvg/LightGlue) — sparse-feature matcher, used with DISK/ALIKED inputs.
- [VPR-Bench](https://github.com/MubarizZaffar/VPR-Bench) — benchmark protocols used for SPEDTest and 17-Places, including their ground-truth contracts.

MAGSAC++ geometric verification and official benchmarks remain third-party techniques and resources with their own scholarly attribution and redistribution conditions. For original citations, licenses, download requirements and versions, consult those projects and the corresponding dataset providers. Avoid assuming that a licence for one upstream codebase also applies to its datasets or model weights.
