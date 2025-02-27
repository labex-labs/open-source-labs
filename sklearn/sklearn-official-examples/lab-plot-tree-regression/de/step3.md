# Regressionmodell anpassen

Wir werden Regressionmodelle mit zwei verschiedenen maximalen Tiefen anpassen: 2 und 5.

```python
regr_1 = DecisionTreeRegressor(max_depth=2)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_1.fit(X, y)
regr_2.fit(X, y)
```
