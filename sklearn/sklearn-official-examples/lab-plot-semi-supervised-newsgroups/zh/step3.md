# 训练和评估监督模型

在这一步中，我们将把数据集拆分为训练集和测试集，然后训练并评估我们在第二步中创建的监督模型管道。

```python
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

# 将数据集拆分为训练集和测试集
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

# 训练并评估监督模型管道
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print(
    "测试集上的微平均 F1 分数：%0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```
