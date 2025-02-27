# 決定木モデルを学習する

このステップでは、元のデータセットに対して決定木モデルを学習します。

```python
reg = DecisionTreeRegressor(min_samples_split=3, random_state=0).fit(X, y)
```
