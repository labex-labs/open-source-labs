# Usar nombres de características para especificar restricciones monotónicas

Si los datos de entrenamiento tienen nombres de características, es posible especificar las restricciones monotónicas pasando un diccionario. Ahora lo demostraremos usando los mismos datos y especificando las restricciones usando nombres de características.

```python
X_df = pd.DataFrame(X, columns=["f_0", "f_1"])

gbdt_with_monotonic_cst_df = HistGradientBoostingRegressor(
    monotonic_cst={"f_0": 1, "f_1": -1}
).fit(X_df, y)

np.allclose(
    gbdt_with_monotonic_cst_df.predict(X_df), gbdt_with_monotonic_cst.predict(X)
)
```
