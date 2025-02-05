# GATE_targeted_abusive_detection

2025/02/05

1. Evaluated granite-guardian-3.1-2b AND -8b model on Yulia, Valadimir and Theretha.
2. The # of abusive tweets are used as the ''ground truth'' data to compare with the granite models' predictions.
--------
Note: The total # of overall is 184,506 in May, but 2,130,344 found on the [Social Media Abuse Dashboard](https://demos.gate.ac.uk/fcdo/platforms/theresa_may/)

| Data           | # of overall | # of abusive  | # of detected  |  # of matching  |  Matching ratio  |
| -----------    | -----------  | ----------- | ----------- | ----------- | ----------- |
| Yulia-2b       |    46,590    |   105       |   27,821    |      104    |    0.3738   |
| Yulia-8b       |    46,590    |   105       |   15,493    |      97     |  **0.6261** |
| Valadimir-2b   |     8,823    |   180       |   3,720     |    174      |    4.6774   |
| Valadimir-8b   |     8,823    |   180       |   1,428     |    156      | **10.9244** |
| May-2b         |    184,506   |  77,886     |   72,205    |    5,044    |   6.9857    |
| May-8b         |    184,506   |  77,886     |   72,205    |    5,044    |   6.9857    |
