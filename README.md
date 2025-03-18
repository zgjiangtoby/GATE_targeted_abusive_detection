# GATE_targeted_abusive_detection

--------
2025/02/05

1. Evaluated granite-guardian-3.1-2b AND -8b model on Yulia Navanalya, Vladimir Soloviev and Theretha May.
2. The # of abusive tweets are used as the ''ground truth'' data to compare with the granite models' predictions.

Note: The total # of overall is 184,506 in May, but 2,130,344 found on the [Social Media Abuse Dashboard](https://demos.gate.ac.uk/fcdo/platforms/theresa_may/)

| Data-Model     | # of overall | # of abusive  | # of detected  |  # of matching  |  Matching ratio (%)  |
| -----------    | -----------  | ----------- | ----------- | ----------- | ----------- |
| Yulia-2b       |    46,590    |   105       |   27,821    |      104    |    0.3738   |
| Yulia-8b       |    46,590    |   105       |   15,493    |      97     |  **0.6261** |
| Vladimir-2b    |     8,823    |   180       |   3,720     |    174      |    4.6774   |
| Vladimir-8b    |     8,823    |   180       |   1,428     |    156      | **10.9244** |
| May-2b         |    184,506   |  77,886     |   72,205    |    5,044    |   6.9857    |
| May-8b         |    184,506   |  77,886     |   23,847    |    4,675    | **19.6041** |

--------
2025/02/10

Using 8b model to infer overall dataset on Yulia, Vladimir, Theretha, Maria, and Liz. Each category is infered per tweet, and the targeted abusive prompt is included. All inferences are maded on two RTX-4090 GPU.

| Data    |  Time   |
| -----------    | -----------  |
| Yulia |  12:59:46 |
| Vladimir | 2:58:15 |
| Theretha| 58:39:40 |
| Maria | 133:57:48 |
| Liz   | 142:04:25 |

--------
2025/03/10
Frist around annotation

| Data    |  annotater1   | annotater2 | Cohen's Kappa |
| -----------    | -----------  |  -----------    | -----------  |
| Yulia | lyz | ljy | 0.2933 |
| Vladimir | xxm | lyz | 0.1343 |
| Theretha| xxm | ljy | 0.2161 |
| Maria | ljy | xxm | 0.3769 |
| Liz   | lyz | ljy | 0.3548 |

--------
2025/03/17
Second around annotation
### note: The uncertain instances are removed from the annotation sets.
| Data    |  annotater1   | annotater2 | Cohen's Kappa |
| -----------    | -----------  |  -----------    | -----------  |
| Yulia | lyz | ljy | 0.6350 |
| Vladimir | xxm | ljy | 0.5537 |
| Theretha| wth | ljy | 0.5201 |
| Maria | wth | xxm | 0.5938 |
| Liz   | wth | xxm | 0.4372 |

--------
2025/03/25
Official annotation (2k per target)

| Data    |  annotater1   | annotater2 | Cohen's Kappa |
| -----------    | -----------  |  -----------    | -----------  |
| Yulia | lyz | ljy |  |
| Vladimir | xxm | lyz |  |
| Theretha| ljy | lyz | |
| Maria | ljy | xxm |  |
| Liz   | wth | xxm |  |
