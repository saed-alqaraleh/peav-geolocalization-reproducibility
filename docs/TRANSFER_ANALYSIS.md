# Operating-point transfer and secondary diagnostics

Frozen development (nine cities; 5,400 queries): Full PEAV Recall@1 0.820926 and mean depth 14.1000; progressive inlier-only Recall@1 0.818333 and mean depth 19.5176.

Protected external evaluation (six datasets, equal-dataset pooling): Full PEAV Recall@1 0.596412 and mean depth 21.2699; progressive inlier-only Recall@1 0.608025 and mean depth 19.2875.

The original fixed-m50 reference has protected Recall@1 0.622547. The Full PEAV difference is -2.6135 percentage points and fails the frozen -0.5 pp noninferiority requirement. All values can be checked with `python scripts/reproduce_all.py`.

Protected Full-minus-inlier continuation AUPRC differences at m=5,10,20 are -0.04718, -0.04160, -0.02502. These are *continuation prediction* diagnostics, not Recall@1 differences. Four separate retriever/backend comparisons have negative Recall@1 point contrasts, three with CIs excluding zero.

The threshold sweeps and supplementary diagnostics under `results/secondary/` are post-protected, descriptive analyses; they are not a new independently confirmed policy selection.
