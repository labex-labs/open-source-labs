# Создание MultiOutputRegressor

Мы создадим `MultiOutputRegressor`, используя регрессора случайного леса в качестве основного оценивающего инструмента. Мы будем использовать те же параметры, что и в шаге 4.

```python
regr_multirf = MultiOutputRegressor(RandomForestRegressor(n_estimators=100, max_depth=max_depth, random_state=0))
regr_multirf.fit(X_train, y_train)
```
