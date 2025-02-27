# 回帰モデルを適合させる

2つの異なる最大深さ：2と5を持つ回帰モデルを適合させます。

```python
regr_1 = DecisionTreeRegressor(max_depth=2)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_1.fit(X, y)
regr_2.fit(X, y)
```
