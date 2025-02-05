# 训练一个决策树模型

在这一步中，我们将在原始数据集上训练一个决策树模型。

```python
reg = DecisionTreeRegressor(min_samples_split=3, random_state=0).fit(X, y)
```
