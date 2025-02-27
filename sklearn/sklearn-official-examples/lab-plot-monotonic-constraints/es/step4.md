# Ajustar un modelo con restricciones monotónicas

Ahora ajustaremos otro modelo a los mismos datos, pero con restricciones monotónicas en las características. Imponeremos una restricción de aumento monotónico en la primera característica y una restricción de disminución monotónica en la segunda característica.

```python
gbdt_with_monotonic_cst = HistGradientBoostingRegressor(monotonic_cst=[1, -1])
gbdt_with_monotonic_cst.fit(X, y)
```
