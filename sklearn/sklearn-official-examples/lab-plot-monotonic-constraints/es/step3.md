# Ajustar un modelo sin restricciones

Ajustaremos un modelo a los datos generados sin ninguna restricción para ver cómo se comporta el modelo sin ninguna limitación.

```python
gbdt_no_cst = HistGradientBoostingRegressor()
gbdt_no_cst.fit(X, y)
```
