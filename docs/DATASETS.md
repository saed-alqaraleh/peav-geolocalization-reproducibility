# Evaluation datasets and ground-truth contracts

| Protected dataset | Physical queries | Positive-relevance contract |
|---|---:|---|
| MSLS validation | 740 | Official validation positives; 25 m criterion |
| Corrected Tokyo 24/7 | 147 | Official positive set excluding junk; corrected 16,140-reference branch |
| Gardens Point | 200 | Frozen one-to-one night-right to day-right identity |
| SPEDTest | 607 | Native VPR-Bench ground-truth pairs |
| AmsterTime | 1,231 | Official old/new identity pair relation |
| 17-Places | 406 | Native VPR-Bench relation, ±3 frames |

**Total:** 3,331 physical queries. Each is evaluated under four paired retriever × local-backend combinations; 13,324 records are not independent query units.

Original VPR-Bench source commit: `77ad30f3684476717188c67d7f3f66be19f832af`. Tokyo 24/7 uses only the corrected branch, not the earlier quarantined branch.

This repository distributes derived numerical outcomes rather than original benchmark images. Consult dataset providers for native data and licensing conditions.
