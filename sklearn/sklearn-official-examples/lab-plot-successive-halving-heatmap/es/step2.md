# Realizar la Búsqueda en Cuadrícula

Utilizaremos la Búsqueda en Cuadrícula para realizar la búsqueda de parámetros en el modelo SVC. Utilizaremos el conjunto de datos sintético generado y la cuadrícula de parámetros generada en el Paso 1.

```python
tic = time()
gs = GridSearchCV(estimator=clf, param_grid=param_grid)
gs.fit(X, y)
gs_time = time() - tic
```
