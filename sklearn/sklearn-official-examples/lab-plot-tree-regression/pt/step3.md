# Ajustar o modelo de regressão

Ajustaremos modelos de regressão com duas profundidades máximas diferentes: 2 e 5.

```python
regr_1 = DecisionTreeRegressor(max_depth=2)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_1.fit(X, y)
regr_2.fit(X, y)
```
