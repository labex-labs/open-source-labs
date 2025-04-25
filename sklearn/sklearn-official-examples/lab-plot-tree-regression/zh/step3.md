# 拟合回归模型

我们将使用两种不同的最大深度（2 和 5）来拟合回归模型。

```python
regr_1 = DecisionTreeRegressor(max_depth=2)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_1.fit(X, y)
regr_2.fit(X, y)
```
