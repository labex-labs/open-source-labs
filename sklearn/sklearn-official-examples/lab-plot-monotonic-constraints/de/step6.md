# Verwendung von Merkmalsnamen zur Angabe von monotonen Einschränkungen

Wenn die Trainingsdaten Merkmalsnamen haben, ist es möglich, die monotonen Einschränkungen durch Angabe eines Wörterbuchs anzugeben. Wir werden dies nun demonstrieren, indem wir die gleichen Daten verwenden und die Einschränkungen mit Hilfe von Merkmalsnamen angeben.

```python
X_df = pd.DataFrame(X, columns=["f_0", "f_1"])

gbdt_with_monotonic_cst_df = HistGradientBoostingRegressor(
    monotonic_cst={"f_0": 1, "f_1": -1}
).fit(X_df, y)

np.allclose(
    gbdt_with_monotonic_cst_df.predict(X_df), gbdt_with_monotonic_cst.predict(X)
)
```
