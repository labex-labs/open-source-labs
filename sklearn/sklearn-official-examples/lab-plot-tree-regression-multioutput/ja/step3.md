# 回帰モデルの適合

このステップでは、回帰モデルを適合させます。異なる最大深さで3つの異なるモデルを適合させるために、sklearn.treeからの`DecisionTreeRegressor`を使用します。

```python
# Fit regression model
regr_1 = DecisionTreeRegressor(max_depth=2)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_3 = DecisionTreeRegressor(max_depth=8)
regr_1.fit(X, y)
regr_2.fit(X, y)
regr_3.fit(X, y)
```
