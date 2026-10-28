# References

Studies the synthetic household generator (notebook 02) is grounded in. All are open access; check each paper's
license before redistributing.

| File | Paper | Study | Use for the generator |
| --- | --- | --- | --- |
| `smullen2020-best-of-both-worlds.pdf` | Smullen, Feng, Zhang, Sadeh. *The Best of Both Worlds: Mitigating Trade-offs Between Accuracy and User Burden in Capturing Mobile App Privacy Preferences.* PoPETs 2020(1) | 994 Android users (MTurk); 6 apps each × 3 permissions × (no purpose + 3 purposes) | Purpose effect (ads, unspecified; "internal" = assumed default); significant background factors; profile accuracy 75–90%; overlapping clusters (silhouette ≈ 0) |
| `naeini2017-iot-privacy-expectations.pdf` | Emami-Naeini, Bhagavatula, Habib, Degeling, Bauer, Cranor, Sadeh. *Privacy Expectations and Preferences in an IoT World.* SOUPS 2017 | 1,007 participants (MTurk); 14 vignettes each from 380 IoT scenarios, 8 factors | Interactions dominate (data type × location, shared × benefit); retention has the smallest effect; majority baseline ≈ 50%, model 76–80% |
| `zhang2021-video-analytics.pdf` | Zhang, Feng, Bauer, Cranor, Das, Sadeh. *"Did you know this camera tracks your mood?": Understanding Privacy Expectations and Preferences in the Age of Video Analytics.* PoPETs 2021(2) | 123 participants, 10-day experience sampling, 2,328 scenarios; 16 purposes × anonymity × retention × sharing × venue | Purpose odds ratios (ads 6–16×, health 29× deny); anonymity and retention weak; comfort–allow correlation 0.60 |
| `liu2016-follow-my-recommendations.pdf` | Liu, Andersen, Schaub, Almuhimedi, Zhang, Sadeh, Acquisti, Agarwal. *Follow My Recommendations: A Personalized Privacy Assistant for Mobile App Permissions.* SOUPS 2016 | 72 users field study, own phones; C4.5 tree, ≤ 5 questions | Questions are aggregated cells (permission × category, permission × purpose), asked only if relevant; 78.7% of recommendations adopted, 5.1% later changed |
| `liu2019-dissertation.pdf` | Bin Liu. *Can Machine Learning Help People Configure Their Mobile App Privacy Settings?* PhD thesis, CMU ISR, 2019 ([KiltHub](https://kilthub.cmu.edu/articles/thesis/Can_Machine_Learning_Help_People_Configure_Their_Mobile_App_Privacy_Settings_/11591340)) | Profiles from rooted-Android settings; Google Play deployment (§6, 156 users) | 7 clusters for 84 users (ch. 4); 6 clusters for 156 users (sizes 17, 39, 25, 21, 17, 37) with per-cluster allow/deny tables |
| `apthorpe2018-smart-home-norms.pdf` | Apthorpe, Shvartzshnaider, Mathur, Reisman, Feamster. *Discovering Smart Home Internet of Things Privacy Norms Using Contextual Integrity.* IMWUT 2(2), 2018 | 1,731 participants (MTurk); 3,840 smart-home flows: device × data × recipient × condition, 1–5 acceptability | Device type effect (thermostat, fitness tracker most accepted; camera, lock, fridge least); function fit (small); ISP/government worst; "not stored", "anonymous" matter in < 10% |

## Files used by notebook 02

| File | Contents |
| --- | --- |
| `crosswalk.csv` | every study term → PPD core terms, with the kind of match (`exact`, `narrower`, `broader`, `partial`, `none`), confidence, whether it is used, and the taxonomy-05 definition it rests on |
| `extracted/apthorpe2018_recipient_tp.csv` | Fig. 3 (top): average acceptability, recipient × transmission principle (80 cells, read from the rendered figure) |
| `extracted/apthorpe2018_sender_attribute.csv` | Fig. 3 (bottom): average acceptability, sender × attribute (48 cells) |
| `extracted/naeini2017_allow_deny.csv` | Table 7: allow/deny mixed-model estimates used (data type, data × house, benefit) |
| `extracted/zhang2021_allow_deny.csv` | Table 6: allow/deny mixed-model estimates (purposes, retention, sharing) |
| `extracted/targets.csv` | calibration and validation targets with their study and section |

Still missing: Zhang, Feng, Das, Bauer, Cranor, Sadeh. *Understanding people's privacy attitudes towards video analytics
technologies.* Technical Report CMU-ISR-20-114, December 2020 (cited by the PoPETs paper; has the clusters; not found
online; link shared by Norman Sadeh in the week 8 meeting chat).
