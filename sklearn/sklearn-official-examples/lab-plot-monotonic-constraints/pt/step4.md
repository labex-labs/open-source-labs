# Ajustar um Modelo com Restrições Monótonas

Agora, ajustaremos outro modelo aos mesmos dados, mas com restrições monótonas nas características. Imporemos uma restrição de aumento monótono na primeira característica e uma restrição de diminuição monótona na segunda característica.

```python
gbdt_with_monotonic_cst = HistGradientBoostingRegressor(monotonic_cst=[1, -1])
gbdt_with_monotonic_cst.fit(X, y)
```
