# Ajustar el modelo de regresión

Ajustaremos modelos de regresión con dos profundidades máximas diferentes: 2 y 5.

```python
regr_1 = DecisionTreeRegressor(max_depth=2)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_1.fit(X, y)
regr_2.fit(X, y)
```
