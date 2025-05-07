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

Multiclass classification
* We conduct a multiclass classification with BERT. Train/val/test split with ratio 8:1:1

| Model |val_acc | val_auc | val_f1 | test_acc | test_auc | test_f1 |
|-------|-------:|--------:|-------:|---------:|---------:|--------:|
| BERT  | 70.85  |  87.03  |  50.96 |  70.95   |  85.86   |   43.97 |


--------
2025/05/07
Dataset statistics
| Category                   | Original     | Train      | Test      |
|----------------------------|--------------|------------|-----------|
| non-abusive                | 5722         | 1800       | 200       |
| religious                  | 2451         | 2206       | 245       |
| attacks_on_credibility     | 2425         | 2182       | 243       |
| radiation_of_threats       | 2311         | 2080       | 231       |
| physical_harm              | 2301         | 2071       | 230       |
| death_threat               | 2288         | 2059       | 229       |
| homophobic                 | 1925         | 1732       | 193       |
| general                    | 1768         | 1591       | 177       |
| misogynistic               | 1625         | 1462       | 163       |
| no-target                  | 1493         | 1344       | 149       |
| sexual_explicit            | 1492         | 1343       | 149       |
| political_sectarian        | 1321         | 1189       | 132       |
| racist                     | 1161         | 1045       | 116       |
| sexual_assault             | 1115         | 1004       | 111       |

### Note: Left columns show deberta-v3-large fine-tuning results; right columns show gemma-3-4b-it instruction-tuning results.
| deberta-v3-large       | Precision | Recall | F1-Score | Support |          | gemma3-4b-it           | Precision | Recall | F1-Score | Support |
|------------------------|-----------|--------|----------|---------|----------|------------------------|-----------|--------|----------|---------|
| attacks_on_credibility | 0.8082    | 0.7284 | 0.7662   | 243     |          | attacks_on_credibility | 0.8186    | 0.7243 | 0.7686   | 243     |
| death_threat           | 0.9389    | 0.9389 | 0.9389   | 229     |          | death_threat           | 0.9237    | 0.9520 | 0.9376   | 229     |
| general                | 0.6580    | 0.7175 | 0.6865   | 177     |          | general                | 0.6250    | 0.6497 | 0.6371   | 177     |
| homophobic             | 0.9795    | 0.9896 | 0.9845   | 193     |          | homophobic             | 0.9795    | 0.9896 | 0.9845   | 193     |
| misogynistic           | 0.9302    | 0.9816 | 0.9552   | 163     |          | misogynistic           | 0.9809    | 0.9448 | 0.9625   | 163     |
| no-target              | 0.9524    | 0.9396 | 0.9459   | 149     |          | no-target              | 0.9444    | 0.9128 | 0.9283   | 149     |
| non-abusive            | 0.7868    | 0.7750 | 0.7809   | 200     |          | non-abusive            | 0.7913    | 0.8150 | 0.8030   | 200     |
| physical_harm          | 0.9824    | 0.9696 | 0.9759   | 230     |          | physical_harm          | 0.9868    | 0.9783 | 0.9825   | 230     |
| political_sectarian    | 0.9333    | 0.9545 | 0.9438   | 132     |          | political_sectarian    | 0.9348    | 0.9773 | 0.9556   | 132     |
| racist                 | 0.9483    | 0.9483 | 0.9483   | 116     |          | racist                 | 0.9483    | 0.9483 | 0.9483   | 116     |
| radiation_of_threats   | 0.9620    | 0.9870 | 0.9744   | 231     |          | radiation_of_threats   | 0.9660    | 0.9827 | 0.9742   | 231     |
| religious              | 0.9918    | 0.9918 | 0.9918   | 245     |          | religious              | 0.9919    | 0.9959 | 0.9939   | 245     |
| sexual_assault         | 0.9720    | 0.9369 | 0.9541   | 111     |          | sexual_assault         | 0.9375    | 0.9459 | 0.9417   | 111     |
| sexual_explicit        | 0.9463    | 0.9463 | 0.9463   | 149     |          | sexual_explicit        | 0.9226    | 0.9597 | 0.9408   | 149     |
|                        |           |        |          |         |          |                        |           |        |          |         |
| accuracy               | -         | -      | 0.9112   | 2568    |          | accuracy               | -         | -      | 0.9097   | 2568    |
| macro avg              | 0.9136    | 0.9146 | 0.9138   | 2568    |          | macro avg              | 0.8501    | 0.8517 | 0.8506   | 2568    |
| weighted avg           | 0.9116    | 0.9112 | 0.9110   | 2568    |          | weighted avg           | 0.9101    | 0.9097 | 0.9094   | 2568    |

### confusion_matrix
<table>
  <tr>
    <td><img src="https://github.com/zgjiangtoby/GATE_targeted_abusive_detection/blob/main/confusion_matrix/deberta-v3-large.png" alt="图片1描述" width="600"></td>
    <td><img src="https://github.com/zgjiangtoby/GATE_targeted_abusive_detection/blob/main/confusion_matrix/gemma3-4b.png" alt="图片2描述" width="600"></td>
  </tr>
  <tr>
    <td align="center">deberta-v3-large</td>
    <td align="center">gemma3-4b-it</td>
  </tr>
</table>

