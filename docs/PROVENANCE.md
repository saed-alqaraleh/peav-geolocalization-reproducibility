# Frozen evidence provenance

## Canonical source records

The protected-evaluation archive `PEAV_FINAL_PROTECTED_EVALUATION_v1.zip` has SHA-256 `f4d7bf6ee0a4c60270a3723be09a6d84fc2141d821de1ce55f630d3d1eddf2af`.

The post-evaluation archive `PEAV_POSTHOC_TRANSFER_EXPLANATION_FINAL_v2_SELF_CONTAINED.zip` has SHA-256 `3692d28807b8b595fc049f92486ce1c902f42aa2c9479d8593116c3fa890fc3d`.

The Phase 1E development-freeze record has SHA-256 `b2a33a6cd0e40b6cdfe8e35ef725619c8479226add226cb7110b111e1e952530`.

`configs/` retains the original protocol and operating-point records. The protected evaluation contains 3,331 unique physical queries and 13,324 matched cell records; the two backends completed their label-blind computations before protected label access. No post-protected controller retuning was performed.

The dataset-level point estimates were independently reconstructed from released cell- and query-level data. Post-protected curves, discrepancy analyses and explanations are secondary and do not change the initial confirmatory verdict.

The notebooks that originally generated the source tables were recovered and source-audited privately. They are not mirrored in this minimal release: their raw, historical Drive assumptions and non-portable intermediate dependencies have not been converted into a safe standalone runtime. Execution of the upstream pipeline requires licensed benchmark inputs and the original model/matching artifacts.
