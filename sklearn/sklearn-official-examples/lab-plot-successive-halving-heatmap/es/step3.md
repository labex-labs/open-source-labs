# Realizar Mitosis Sucesiva

Ahora realizaremos la búsqueda de parámetros utilizando Mitosis Sucesiva en el mismo modelo SVC y conjunto de datos utilizados en el Paso 2.

```python
tic = time()
gsh = HalvingGridSearchCV(
    estimator=clf, param_grid=param_grid, factor=2, random_state=rng
)
gsh.fit(X, y)
gsh_time = time() - tic
```
