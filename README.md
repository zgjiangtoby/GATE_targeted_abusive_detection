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
2025/03/31
Official annotation (2k per target)

| Data    |  annotater1   | annotater2 | Cohen's Kappa |
| -----------    | -----------  |  -----------    | -----------  |
| Yulia | lyz | ljy | 0.6637 |
| Vladimir | xxm | lyz | 0.7235 |
| Theretha| ljy | lyz | 0.7631 |
| Maria | ljy | xxm | 0.7277 |
| Liz   | wth | xxm | 0.6699 |


Label statistics

|     |  1-label   | 2-labels | 3-labels | 4-labels |  5-labels  |  total |
| -----------    | -----------  |  -----------    | -----------  |  -----------  |  -----------  | -----------  |
| Liz |1139	 | 762 | 84	| 11	| 0  | 1996 |  
| Maria | 1376 |	545 |	57 | 9	| 0 | 1987 |
| May |	1503 | 472 | 18 |	4	| 0 |	1997 |
| Vladimir	| 1360 | 496 | 106 | 21 |	5	| 1988 |
| Yulia |	1330 |	603	|27 |	2	| 1	| 1963 |
| TOTAL| 6708	| 2878 | 292 |	47 |	6 |	9931 |

Human vs Machine accuracies

| Data | Binary | Multi |
| -----------    | -----------  |  -----------    |
|Liz |  80.51 |  39.98 |
|Maria | 89.63 | 51.17 |
|May | 94.19 | 52.40 |
|Vladimir | 91.09 | 46.58 |
|Yulia | 78.45 | 38.00 |

*note: Binary means the accuracy is calculated by only consider abusive and non-abusive posts. Multi denotes the accuracy of multi-label classification, in which the machine predicted label is matched with at least one human annotated label. Non-abusive posts are removed in Multi.


2025/04/16

Label statistics

| Name   | death_threat | sexual_assault | Sexual_explicit | physical_harm | radiation_of_threats | attacks_on_credibility | misogynistic | homophobic | religious | political_sectarian | racist | general | non-abusive | no-target | unidentified-targets | Total |
|--------|-------------:|---------------:|----------------:|--------------:|---------------------:|-----------------------:|-------------:|-----------:|----------:|-------------------:|-------:|--------:|------------:|----------:|---------------------:|-------:|
| Liz    | 13           | 5              | 9               | 3             | 1                    | 463                    | 12           | 2          | 4         | 40                 | 29     | 273     | 1125        | 6         | 11                    | 1996         |
| Maria  | 12           | 13             | 41              | 16            | 2                    | 229                    | 13           | 9          | 1         | 0                  | 10     | 387     | 1213        | 8         | 32                   | 1986         |    
| May    | 18           | 4              | 26              | 3             |0                     | 280                    | 29           | 4          | 25        | 47                 | 20     | 403     | 1122        | 0         | 16                   | 1997         |
| Vala   | 91           | 13             | 63              | 22            | 85                   | 41                     | 39           | 15         | 4         | 4                  | 52     | 384     | 1085        | 237       | 43                    | 2178         |
| Yulia  | 41           | 15             | 32              | 6             | 15                   | 181                    | 19           | 2          | 3         | 16                 | 42     | 321     | 1177        | 2         | 91                    | 1963         |
| Total  | 175          | 50             | 171             | 50            | 103                  | 1194                   | 112          | 32         | 37        | 107                | 153    | 1768    | 5722        | 253       | 193                   | 10120        |
