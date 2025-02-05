# 在离散化数据集上训练决策树模型

在这一步中，我们将在离散化后的数据集上训练一个决策树模型。

```python
reg = DecisionTreeRegressor(min_samples_split=3, random_state=0).fit(X_binned, y)
```
