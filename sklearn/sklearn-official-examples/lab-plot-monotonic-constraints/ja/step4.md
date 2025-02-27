# 単調制約付きでモデルをフィットさせる

今度は同じデータに対して、特徴量に単調制約を加えた別のモデルをフィットさせます。最初の特徴量には単調増加制約を、2番目の特徴量には単調減少制約を課します。

```python
gbdt_with_monotonic_cst = HistGradientBoostingRegressor(monotonic_cst=[1, -1])
gbdt_with_monotonic_cst.fit(X, y)
```
