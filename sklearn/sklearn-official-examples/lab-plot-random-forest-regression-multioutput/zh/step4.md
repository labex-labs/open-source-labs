# 创建随机森林回归器

我们将使用 scikit-learn 的`RandomForestRegressor`创建一个最大深度为 30 且有 100 个估计器的随机森林回归器。

```python
max_depth = 30
regr_rf = RandomForestRegressor(n_estimators=100, max_depth=max_depth, random_state=2)
regr_rf.fit(X_train, y_train)
```
