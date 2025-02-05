# 拟合回归模型

在这一步中，我们将拟合回归模型。我们将使用来自scikit-learn库中sklearn.tree的`DecisionTreeRegressor`来拟合三个具有不同最大深度的不同模型。

```python
# 拟合回归模型
regr_1 = DecisionTreeRegressor(max_depth=2)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_3 = DecisionTreeRegressor(max_depth=8)
regr_1.fit(X, y)
regr_2.fit(X, y)
regr_3.fit(X, y)
```
