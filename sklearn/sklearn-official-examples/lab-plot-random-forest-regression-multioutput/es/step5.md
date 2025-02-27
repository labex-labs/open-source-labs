# Crear MultiOutputRegressor

Crearemos un `MultiOutputRegressor` utilizando un regresor de bosque aleatorio como estimador subyacente. Utilizaremos los mismos parámetros que en el Paso 4.

```python
regr_multirf = MultiOutputRegressor(RandomForestRegressor(n_estimators=100, max_depth=max_depth, random_state=0))
regr_multirf.fit(X_train, y_train)
```
