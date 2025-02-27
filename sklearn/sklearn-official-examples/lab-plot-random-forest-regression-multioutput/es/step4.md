# Crear un regresor de bosque aleatorio

Crearemos un regresor de bosque aleatorio con una profundidad máxima de 30 y 100 estimadores utilizando `RandomForestRegressor` de scikit-learn.

```python
max_depth = 30
regr_rf = RandomForestRegressor(n_estimators=100, max_depth=max_depth, random_state=2)
regr_rf.fit(X_train, y_train)
```
