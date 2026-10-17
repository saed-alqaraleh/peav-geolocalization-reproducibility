# Upstream software, methods, and benchmark attribution

This repository includes numerical replay scripts and frozen derived evaluation records. Original pretrained models, third-party image datasets, and the complete upstream image-matching pipeline are not redistributed here. The method links below identify original research sources and corresponding implementation repositories.

| Component | Scholarly source | Upstream implementation |
| --- | --- | --- |
| CosPlace global retrieval | [Berton et al., CVPR 2022](https://openaccess.thecvf.com/content/CVPR2022/html/Berton_Rethinking_Visual_Geo-Localization_for_Large-Scale_Applications_CVPR_2022_paper.html) | [gmberton/CosPlace](https://github.com/gmberton/CosPlace) |
| R2Former retrieval branch | [Zhu et al., CVPR 2023](https://openaccess.thecvf.com/content/CVPR2023/html/Zhu_R2Former_Unified_Retrieval_and_Reranking_Transformer_for_Place_Recognition_CVPR_2023_paper.html) | [Jeff-Zilence/R2Former](https://github.com/Jeff-Zilence/R2Former) |
| DISK keypoints and descriptors | [Tyszkiewicz et al., NeurIPS 2020](https://proceedings.neurips.cc/paper/2020/hash/a42a596fc71e17828440030074d15e74-Abstract.html) | Follow the author's released implementation and licensing terms |
| ALIKED keypoints and descriptors | [Zhao et al., IEEE TIM 2023](https://doi.org/10.1109/TIM.2023.3271000) | [shiaoming/ALIKED](https://github.com/Shiaoming/ALIKED) |
| LightGlue matching | [Lindenberger et al., ICCV 2023](https://openaccess.thecvf.com/content/ICCV2023/html/Lindenberger_LightGlue_Local_Feature_Matching_at_Light_Speed_ICCV_2023_paper.html) | [cvg/LightGlue](https://github.com/cvg/LightGlue) |
| MAGSAC++ robust estimation | [Barath et al., CVPR 2020](https://openaccess.thecvf.com/content_CVPR_2020/html/Barath_MAGSAC_a_Fast_Reliable_and_Accurate_Robust_Estimator_CVPR_2020_paper.html) | Use the applicable original implementation and license |
| SPEDTest and 17-Places protocols | Original VPR-Bench ground truth, pinned source commit `77ad30f3684476717188c67d7f3f66be19f832af` | [MubarizZaffar/VPR-Bench](https://github.com/MubarizZaffar/VPR-Bench) |

The [AmsterTime dataset](https://doi.org/10.4121/19580806) is available through 4TU.ResearchData. The remaining benchmark datasets should be obtained from their respective providers using the protocols in [DATASETS.md](DATASETS.md).

Third-party implementations, pretrained weights, benchmark images, and annotations each retain their own licensing and redistribution conditions. The code included here is limited to numerical replay and verification of frozen derived outputs. Original papers and upstream projects should be credited when their resources are used.
