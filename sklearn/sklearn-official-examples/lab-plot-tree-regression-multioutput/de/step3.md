# Regressionmodell anpassen

In diesem Schritt werden wir Regressionmodelle anpassen. Wir werden `DecisionTreeRegressor` aus sklearn.tree verwenden, um drei verschiedene Modelle mit unterschiedlichen maximalen Tiefen anzupassen.

```python
# Fit regression model
regr_1 = DecisionTreeRegressor(max_depth=2)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_3 = DecisionTreeRegressor(max_depth=8)
regr_1.fit(X, y)
regr_2.fit(X, y)
regr_3.fit(X, y)
```
