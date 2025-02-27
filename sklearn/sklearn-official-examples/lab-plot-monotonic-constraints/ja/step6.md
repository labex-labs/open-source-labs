# 特徴量名を使って単調制約を指定する

学習データに特徴量名がある場合、辞書を渡すことで単調制約を指定することができます。ここでは、同じデータを使って特徴量名を使って制約を指定することを示します。

```python
X_df = pd.DataFrame(X, columns=["f_0", "f_1"])

gbdt_with_monotonic_cst_df = HistGradientBoostingRegressor(
    monotonic_cst={"f_0": 1, "f_1": -1}
).fit(X_df, y)

np.allclose(
    gbdt_with_monotonic_cst_df.predict(X_df), gbdt_with_monotonic_cst.predict(X)
)
```
