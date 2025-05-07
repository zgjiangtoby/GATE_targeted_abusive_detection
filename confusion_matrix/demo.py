import json
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

# 读取你的JSON文件（请替换为你的文件名）
with open('predictions_20250430_010841.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 提取真实标签和预测标签
y_true = [item['output'] for item in data]
y_pred = [item['predict'] for item in data]

# 获取所有可能的标签（保持顺序一致）
labels = sorted(list(set(y_true + y_pred)))



cm = confusion_matrix(y_true, y_pred, labels=labels)
df_cm = pd.DataFrame(cm, index=labels, columns=labels)

plt.figure(figsize=(12, 10))
sns.heatmap(df_cm, annot=True, fmt="d", cmap="Blues", cbar=False)
plt.title("confusion_matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.tight_layout()
plt.show()
