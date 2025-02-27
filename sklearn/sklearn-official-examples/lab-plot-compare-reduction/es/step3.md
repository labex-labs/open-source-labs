# Crear un objeto GridSearchCV y ajustar los datos

Crearemos un objeto `GridSearchCV` utilizando la tubería y la cuadrícula de parámetros que definimos en el paso anterior. Luego ajustaremos los datos al objeto.

```python
grid = GridSearchCV(pipe, n_jobs=1, param_grid=param_grid)
grid.fit(X, y)
```
