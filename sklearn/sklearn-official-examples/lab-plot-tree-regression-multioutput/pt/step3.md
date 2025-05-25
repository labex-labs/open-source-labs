# Ajustar o Modelo de Regressão

Neste passo, ajustaremos modelos de regressão. Usaremos `DecisionTreeRegressor` de `sklearn.tree` para ajustar três modelos diferentes com profundidades máximas diferentes.

```python
# Ajustar o modelo de regressão
regr_1 = DecisionTreeRegressor(max_depth=2)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_3 = DecisionTreeRegressor(max_depth=8)
regr_1.fit(X, y)
regr_2.fit(X, y)
regr_3.fit(X, y)
```
