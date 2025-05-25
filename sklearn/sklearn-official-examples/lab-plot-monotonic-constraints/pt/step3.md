# Ajustar um Modelo Sem Restrições

Vamos ajustar um modelo aos dados gerados sem quaisquer restrições para observar o desempenho do modelo sem limitações.

```python
gbdt_no_cst = HistGradientBoostingRegressor()
gbdt_no_cst.fit(X, y)
```
