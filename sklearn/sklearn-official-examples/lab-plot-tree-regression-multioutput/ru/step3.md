# Настройка регрессионной модели

В этом шаге мы настроим регрессионные модели. Мы будем использовать `DecisionTreeRegressor` из sklearn.tree для настройки трех разных моделей с разной максимальной глубиной.

```python
# Fit regression model
regr_1 = DecisionTreeRegressor(max_depth=2)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_3 = DecisionTreeRegressor(max_depth=8)
regr_1.fit(X, y)
regr_2.fit(X, y)
regr_3.fit(X, y)
```
