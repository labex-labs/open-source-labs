# Использование имен характеристик для указания монотонных ограничений

Если в обучающих данных есть имена характеристик, то можно указать монотонные ограничения, передав словарь. Теперь мы это покажем, используя те же данные и указывая ограничения с использованием имен характеристик.

```python
X_df = pd.DataFrame(X, columns=["f_0", "f_1"])

gbdt_with_monotonic_cst_df = HistGradientBoostingRegressor(
    monotonic_cst={"f_0": 1, "f_1": -1}
).fit(X_df, y)

np.allclose(
    gbdt_with_monotonic_cst_df.predict(X_df), gbdt_with_monotonic_cst.predict(X)
)
```
