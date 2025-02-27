# Создание регрессора случайного леса

Мы создадим регрессора случайного леса с максимальной глубиной 30 и 100 оценщиками с использованием `RandomForestRegressor` из scikit-learn.

```python
max_depth = 30
regr_rf = RandomForestRegressor(n_estimators=100, max_depth=max_depth, random_state=2)
regr_rf.fit(X_train, y_train)
```
