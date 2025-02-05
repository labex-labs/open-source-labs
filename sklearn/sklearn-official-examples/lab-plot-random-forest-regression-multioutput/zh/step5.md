# 创建多输出回归器

我们将使用随机森林回归器作为基础估计器来创建一个`MultiOutputRegressor`。我们将使用与步骤4中相同的参数。

```python
regr_multirf = MultiOutputRegressor(RandomForestRegressor(n_estimators=100, max_depth=max_depth, random_state=0))
regr_multirf.fit(X_train, y_train)
```
