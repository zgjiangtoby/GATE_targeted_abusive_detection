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

### Dataset statistics
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

--------
2025/05/09
### L2D method

- using xlm-roberta-base and Phi-3-mini-128k-instruct (k=30, n=8)
- using deberta-v3-large and Phi-3-mini-128k-instruct (k=30, n=8)
- using deberta-v3-large and gemma2-9b-it (k=30, n=8)

| Metric         | XLM + Phi-3 | DeBERTa + Phi-3 | DeBERTa + Gemma2 |
|----------------|------------|----------------|----------------|
| Accuracy       | 0.83       | 0.82           | 0.87           |
| Macro Avg      | 0.84       | 0.83           | 0.86           |
| Weighted Avg   | 0.83       | 0.83           | 0.86           |
| Support        | 2554       | 2548           | 2551           |

--------
2025/06/10

Target：
@VRSoloviev：
**User Profile: Vladimir Rudolʹfovich Solovyov (@VRSoloviev)**
Vladimir Rudolʹfovich Solovyov is a Russian male media figure known for his roles as a television host, radio commentator, and political columnist. He is a prominent voice closely aligned with the Russian government and is widely recognized for amplifying pro-Kremlin narratives. Though not formally affiliated with a political party, Solovyov maintains ideological proximity to United Russia and operates as a consistent defender of President Vladimir Putin’s policies, particularly in matters of foreign affairs and national identity.
Solovyov publicly identifies with Judaism and has acknowledged his Jewish heritage. He has been married three times and is currently married to psychologist Elga Sepp; he has eight children.
His commentary is characterized by a strongly nationalistic and adversarial tone. He is known for endorsing Russia’s military actions abroad and for promoting rhetoric that frequently aligns with state strategic messaging. As a result, Solovyov has faced international sanctions, including travel restrictions and asset freezes, due to his role in supporting or legitimizing aggressive state behavior, particularly in the context of the Russia-Ukraine conflict.
Solovyov’s close alignment with state messaging, coupled with his frequent appearances on state-controlled media, positions him as an influential figure in Russia’s domestic information space. At the same time, he has been widely criticized by international observers and civil society groups for spreading disinformation and fostering hostility through inflammatory speech. These dynamics have made him a central—but highly polarizing—actor in Russia’s contemporary media and political landscape.

@yulia_navalnaya
**User Profile: Yulia Borisovna Navalnaya (@yulia_navalnaya)**
Yulia Navalnaya is a Russian female public figure and economist who has emerged as a leading opposition voice following the death of her husband, Alexei Navalny. Although she once avoided the spotlight, she was known as his trusted confidante and played a decisive role during his poisoning crisis in 2020 by orchestrating his evacuation to Germany and confronting authorities.
Politically, Navalnaya was a member of the liberal, centre‑left Yabloko party from 2000 to 2011, but largely stayed out of active politics until she stepped into the public arena to continue her husband’s anti-corruption and pro-democracy agenda. She currently chairs the Human Rights Foundation and leads the Anti-Corruption Foundation, maintaining a dormant formal party association while driving the broader opposition movement. 
From her background, Navalnaya is the mother of two children, born circa 2001 and 2008, and worked earlier in banking and trade roles before dedicating herself to family life. Though she now lives abroad for safety, she continues to represent a democratic alternative to Putin’s regime, vocally condemning his governance and calling for political reform in Russia.
Navalnaya is widely seen by international audiences as a resilient figure of moral courage and democratic values, though her rise also invites scrutiny about continuity with her late husband’s leadership and the challenge of forging her own political identity in Russia’s repressive environment .

@theresa_may
**User Profile: Theresa May (@theresa_may)**
Theresa Mary May is a British female political figure affiliated with the Conservative Party, best known for serving as the United Kingdom’s Prime Minister from July 2016 to July 2019, and previously as Home Secretary from 2010 to 2016. Although she never formally led a party beyond her role within the Conservative Party, her leadership was closely tied to party initiatives such as drafting and executing Brexit legislation, including the European Union (Notification of Withdrawal) Act 2017 and European Union (Withdrawal) Act 2018.
May has been a Member of Parliament for Maidenhead from 1997 until stepping down at the 2024 general election, and in 2002–2003 she became the first female Chair of the Conservative Party. Earlier political roles included positions within the Shadow Cabinet such as Shadow Secretary for Education, Transport, the Family, and Culture.
She grew up as the only child of an Anglican vicar, remains a committed member of the Church of England in the Anglo‑Catholic tradition, and regularly attends church. Married since 1980 to Philip May, they have no children.
During her tenure as Home Secretary, May introduced major reforms including the National Crime Agency and Modern Slavery Act, and overhauled police oversight. As Prime Minister, she led the UK’s Brexit negotiations, took legal steps to invoke Article 50, and pursued policies on net-zero emissions, racial auditing, mental health funding expansion, and investigatory powers legislation.
While praised for determination and public service ethos, her Brexit strategy also attracted criticism and parliamentary setbacks, contributing to intra-party conflict and her eventual resignation . Post-premiership, May has authored a book on institutional power abuse and remains active in public speaking and advocacy on modern slavery and justice issues.



@trussliz
**User Profile: Theresa May (@trussliz)**
Mary Elizabeth Truss, known as Liz Truss, is a British female politician affiliated with the Conservative Party. She briefly served as Prime Minister of the United Kingdom from September to October 2022, making her the shortest-serving prime minister in British history. Prior to that, she held multiple senior cabinet positions, including Secretary of State for International Trade, Foreign Secretary, and Chief Secretary to the Treasury.
Truss has been the Member of Parliament for South West Norfolk since 2010. Ideologically, she has been associated with libertarian-leaning economic policies, advocating for deregulation, tax cuts, and a minimal state. Her tenure as Prime Minister was marked by a controversial "mini-budget" that triggered financial market turmoil and widespread criticism, leading to her resignation after just 49 days in office.
Religiously, Truss was raised in a liberal-left household with no strong religious affiliation, and she has not been prominently associated with any faith tradition. She is married to Hugh O’Leary, an accountant, and they have two daughters.
Though her premiership was short-lived, Truss continues to engage in political commentary and policy advocacy, particularly on issues related to economic freedom, foreign policy, and opposition to what she describes as "left-wing cultural orthodoxy."

@mariaressa
**User Profile: Maria Angelita Ressa (@maria_ressa)**
Maria Ressa is a Filipino–American investigative journalist, co‑founder and CEO of Rappler, the Manilla‑based digital news outlet renowned for its focus on accountability, social media manipulation, and democratic resilience. With nearly four decades of experience—including key roles as CNN bureau chief in Manila and Jakarta—she has been a persistent critic of authoritarian governance and human rights violations in the Philippines.
Ressa holds dual Filipino and US citizenship. She is married (spousal details not prominently disclosed) and maintains a low‑profile personal life to safeguard privacy.
Her work has been recognized globally: she received the 2021 Nobel Peace Prize “for efforts to safeguard freedom of expression, which is a precondition for democracy and lasting peace”. She has also been named Time’s Person of the Year (2018), among its 100 Most Influential People (2019), and has won numerous awards for press freedom and resilience .
Ressa’s career has been marked by both professional acclaim and legal struggle: her outlet Rappler faced government harassment under Rodrigo Duterte’s administration, leading to criminal charges such as cyber-libel and alleged tax violations—widely regarded as politically motivated. International human rights organizations have condemned these actions as part of a broader attack on media independence.
Currently a professor of professional practice and distinguished fellow at Columbia SIPA, Ressa continues to advocate for democratic reforms, ethical journalism, and accountability for digital-era disinformation.


--------
2025/09/08

# 零样本
首先将数据集拆分成五个同人名数据集，然后我们分别结合五个人的人物画像，对五个同人名数据集单独进行实验。随后根据大模型的预测结果，我们得到了687条大模型预测错误的数据，我对这687条数据进行了错误分析，查看是否存在人工标错数据的可能，然后发现其中有179条数据是我们人工标注存在问题，大模型预测的结果是对的，而我们的人工标注结果是错的，我对这179条数据进行了重新标注，随后得到一个最终的预测结果。实验数据及结果如表1所示。
| target            | 总样本数  | 正确样本数   | 准确率   | 标错样本数 | 纠错后正确样本数 | 纠错后准确率 |
|------------------ |----------|-------------|---------|------------|-----------------|------------|
| @mariaressa       | 569      | 469         | 82.43   | 34         | 503             | 88.4       |                       
| @theresa_may      | 880      | 769         | 87.39   | 28         | 797             | 90.57      |                        
| @trussliz         | 860      | 669         | 77.79   | 26         | 695             | 80.81      |                         
| @RSoloviev        | 787      | 733         | 93.14   | 14         | 747             | 94.92      |                        
| @Julia_navalnaya  | 718      | 487         | 67.83   | 7          | 564             | 78.55      |                         
| sum               | 3814     | 3127        | 81.99   | 179        | 3306            | 86.68      |  
<div align="center">表1</div>

得到新的纠错后数据集后重新跑了一下实验，得到实验结果如表2所示。
| Model | Class | precision | recall | fl-score | support |
|-------|-------|-----------|--------|----------|---------|
| **Qwen-2.5-14B (纠错前)** | | | | | |
| | unidentified-targets | 0.13 | 0.53 | 0.21 | 176 |
| | target-abusive | 0.97 | 0.83 | 0.9 | 3638 |
| | accuracy | | | 0.82 | 3814 |
| | macro avg | 0.55 | 0.68 | 0.56 | 3814 |
| | weighted avg | 0.93 | 0.82 | 0.87 | 3814 |
| **Qwen-2.5-14B (纠错后)** | | | | | |
| | unidentified-targets | 0.35 | 0.68 | 0.47 | 317 |
| | target-abusive | 0.97 | 0.89 | 0.93 | 3497 |
| | accuracy | | | 0.87 | 3814 |
| | macro avg | 0.66 | 0.78 | 0.7 | 3814 |
| | weighted avg | 0.92 | 0.87 | 0.89 | 3814 |
<div align="center">表2</div>

对于零样本，我们还做了一个小实验，在input内容后加一个label标签，实验结果表明，不加标签的实验结果比加标签后的实验结果相差不大，但总体稍差。实验结果如表3所示。
| Model | Class | precision | recall | f1-score | support |
|-------|-------|-----------|--------|----------|---------|
| **Qwen-2.5-14B(纠错后，加label)** | | | | | |
| | unidentified-targets | 0.3 | 0.8 | 0.44 | 317 |
| | target-abusive | 0.98 | 0.83 | 0.9 | 3497 |
| | accuracy | | | 0.83 | 3814 |
| | macro avg | 0.64 | 0.82 | 0.67 | 3814 |
| | weighted avg | 0.92 | 0.83 | 0.86 | 3814 |
<div align="center">表3</div>

# 少样本
随后，我们在此基础上用新的数据集和同样的方法进行少样本实验。实验结果如表4所示。
| Model | Class | precision | recall | fl-score | support |
|-------|-------|-----------|--------|----------|---------|
| **8-shot Qwen-2.5-14B** | | | | | |
| | unidentified-targets | 0.33 | 0.66 | 0.47 | 317 |
| | target-abusive | 0.98 | 0.93 | 0.91 | 3497 |
| | accuracy | | | 0.85 | 3814 |
| | macro avg | 0.69 | 0.88 | 0.85 | 3814 |
| | weighted avg | 0.83 | 0.85 | 0.85 | 3814 |
| **Qwen-2.5-14B (label)** | | | | | |
| | unidentified-targets | 0.27 | 0.62 | 0.4 | 317 |
| | target-abusive | 0.97 | 0.91 | 0.89 | 3497 |
| | accuracy | | | 0.81 | 3814 |
| | macro avg | 0.64 | 0.85 | 0.81 | 3814 |
| | weighted avg | 0.78 | 0.81 | 0.81 | 3814 |
<div align="center">表4</div>

随后，我们更新了一下样本提示及回复结果，进行了样本的一个新实验，我们加上了non-abusive这个标签，二分类任务现在变成了一个三分类任务，我们将response里label中的结果转换成0,1,2，然后进行评估，评估结果如表5所示。
| Model | Class | precision | recall | f1-score | support |
|-------|-------|-----------|--------|----------|---------|
| **Qwen-2.5-14B** | | | | | |
| | unidentified-targets | 0.08 | 0.13 | 0.1 | 317 |
| | target-abusive | 0.72 | 0.93 | 0.81 | 3497 |
| | non-abusive | 0.96 | 0.69 | 0.8 | 4206 |
| | accuracy | | | 0.77 | 8020 |
| | macro avg | 0.59 | 0.58 | 0.57 | 8020 |
| | weighted avg | 0.82 | 0.77 | 0.78 | 8020 |
<div align="center">表5</div>

随后我们还是将non-abusive这个标签去掉，还是做一个二分类任务，分别进行了1,3,5个样本的实验，实验结果如表6所示。
| Shot Type | Model | Class | precision | recall | f1-score | support |
|-----------|-------|-------|-----------|--------|----------|---------|
| **1-shot** | Qwen-2.5-14B | unidentified-targets | 0.14 | 0.13 | 0.14 | 317 |
| | | target-abusive | 0.92 | 0.93 | 0.92 | 3497 |
| | | accuracy | | | 0.86 | 3814 |
| | | macro avg | 0.53 | 0.53 | 0.53 | 3814 |
| | | weighted avg | 0.86 | 0.86 | 0.86 | 3814 |
| **3-shot** | Qwen-2.5-14B | unidentified-targets | 0.15 | 0.58 | 0.24 | 317 |
| | | target-abusive | 0.95 | 0.69 | 0.8 | 3497 |
| | | accuracy | | | 0.68 | 3814 |
| | | macro avg | 0.55 | 0.53 | 0.52 | 3814 |
| | | weighted avg | 0.88 | 0.68 | 0.75 | 3814 |
| **5-shot** | Qwen-2.5-14B | unidentified-targets | 0.15 | 0.49 | 0.23 | 317 |
| | | target-abusive | 0.94 | 0.76 | 0.84 | 3497 |
| | | accuracy | | | 0.74 | 3814 |
| | | macro avg | 0.55 | 0.62 | 0.54 | 3814 |
| | | weighted avg | 0.88 | 0.74 | 0.79 | 3814 |
<div align="center">表6</div>

我们发现这些实验结果分数都较低，我们猜想是不是用户画像影响了实验结果，我们在新的少样本实验基础上，把用户画像也添加上去，分别也进行了1,3,5shot实验，实验结果如表7所示。

| Model | Class | precision | recall | f1-score | support |
|-------|-------|-----------|--------|----------|---------|
| **Qwen-2.5-14B (add_profiles) 1** | | | | | |
| | unidentified-targets | 0.27 | 0.4 | 0.32 | 317 |
| | target-abusive | 0.94 | 0.9 | 0.92 | 3497 |
| | accuracy | | | 0.86 | 3814 |
| | macro avg | 0.61 | 0.65 | 0.62 | 3814 |
| | weighted avg | 0.89 | 0.86 | 0.87 | 3814 |
| **Qwen-2.5-14B (add_profiles) 3** | | | | | |
| | unidentified-targets | 0.21 | 0.58 | 0.31 | 317 |
| | target-abusive | 0.95 | 0.8 | 0.87 | 3497 |
| | accuracy | | | 0.78 | 3814 |
| | macro avg | 0.58 | 0.69 | 0.59 | 3814 |
| | weighted avg | 0.89 | 0.78 | 0.82 | 3814 |
| **Qwen-2.5-14B (add_profiles) 5** | | | | | |
| | unidentified-targets | 0.2 | 0.57 | 0.29 | 317 |
| | target-abusive | 0.95 | 0.79 | 0.86 | 3497 |
| | accuracy | | | 0.77 | 3814 |
| | macro avg | 0.57 | 0.68 | 0.58 | 3814 |
| | weighted avg | 0.89 | 0.77 | 0.81 | 3814 |
<div align="center">表7</div>
我们发现随着shot数量增加，f1分数反倒降低（但是相比之前没有加user profiles的结果有一定提升）。

# 微调
在进行了少样本学习后，我们开始尝试用微调来进行该任务，我们首先微调了三个小模型，我们还是将non-abusive这个类加到分类当中，将该任务视作一个三分类任务，实验结果如表8所示。
| Model | Class | precision | recall | f1-score | support |
|-------|-------|-----------|--------|----------|---------|
| **mdeberta-v3-base (微调epoch20)** | | | | | |
| | unidentified-targets | 0.2592 | 0.4516 | 0.3294 | 317 |
| | target-abusive | 0.8351 | 0.8828 | 0.8583 | 3497 |
| | non-abusive | 0.9047 | 0.8123 | 0.856 | 4206 |
| | accuracy | | | 0.8291 | 8020 |
| | macro avg | 0.6663 | 0.7156 | 0.6812 | 8020 |
| | weighted avg | 0.8494 | 0.8291 | 0.8367 | 8020 |
| **mt5-base-wikinewssum-all-languages (微调epoch30)** | | | | | |
| | unidentified-targets | 0.4347 | 0.3225 | 0.3703 | 317 |
| | target-abusive | 0.8031 | 0.8742 | 0.8372 | 3497 |
| | non-abusive | 0.8793 | 0.8313 | 0.8547 | 4206 |
| | accuracy | | | 0.8304 | 8020 |
| | macro avg | 0.7057 | 0.676 | 0.6874 | 8020 |
| | weighted avg | 0.8289 | 0.8304 | 0.8283 | 8020 |
| **multilingual-e5-base (微调epoch10)** | | | | | |
| | unidentified-targets | 0.5882 | 0.3225 | 0.4166 | 317 |
| | target-abusive | 0.8457 | 0.8771 | 0.8611 | 3497 |
| | non-abusive | 0.8791 | 0.8812 | 0.8801 | 4206 |
| | accuracy | | | 0.8578 | 8020 |
| | macro avg | 0.771 | 0.6936 | 0.7193 | 8020 |
| | weighted avg | 0.8533 | 0.8578 | 0.8539 | 8020 |
<div align="center">表8</div>
从表8中，我们可以看到，multilingual-e5-base（微调epoch10）该模型10个epoch的时候，结果最好，f1分数达到了0.7193。

