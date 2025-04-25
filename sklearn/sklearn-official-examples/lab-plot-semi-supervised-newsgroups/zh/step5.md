# 训练和评估自训练模型

在这一步中，我们将对 20% 的已标注数据使用自训练方法。我们将随机选择 20% 的已标注数据，在这些数据上训练模型，然后使用该模型为其余未标注数据预测标签。

```python
import numpy as np

# 选择 20% 的训练数据
y_mask = np.random.rand(len(y_train)) < 0.2
X_20, y_20 = map(
    list, zip(*((x, y) for x, y, m in zip(X_train, y_train, y_mask) if m))
)

# 将未掩码的子集设置为未标注
y_train[~y_mask] = -1

# 训练并评估自训练管道
st_pipeline.fit(X_train, y_train)
y_pred = st_pipeline.predict(X_test)
print(
    "测试集上的微平均 F1 分数：%0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```
