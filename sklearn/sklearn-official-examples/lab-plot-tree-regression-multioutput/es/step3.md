# Ajustar el modelo de regresión

En este paso, ajustaremos los modelos de regresión. Utilizaremos `DecisionTreeRegressor` de sklearn.tree para ajustar tres modelos diferentes con diferentes profundidades máximas.

```python
# Fit regression model
regr_1 = DecisionTreeRegressor(max_depth=2)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_3 = DecisionTreeRegressor(max_depth=8)
regr_1.fit(X, y)
regr_2.fit(X, y)
regr_3.fit(X, y)
```
