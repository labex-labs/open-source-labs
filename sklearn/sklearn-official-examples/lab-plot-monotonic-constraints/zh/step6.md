# 使用特征名称指定单调约束

如果训练数据有特征名称，则可以通过传递字典来指定单调约束。现在我们将使用相同的数据并通过特征名称指定约束来演示这一点。

```python
X_df = pd.DataFrame(X, columns=["f_0", "f_1"])

gbdt_with_monotonic_cst_df = HistGradientBoostingRegressor(
    monotonic_cst={"f_0": 1, "f_1": -1}
).fit(X_df, y)

np.allclose(
    gbdt_with_monotonic_cst_df.predict(X_df), gbdt_with_monotonic_cst.predict(X)
)
```
