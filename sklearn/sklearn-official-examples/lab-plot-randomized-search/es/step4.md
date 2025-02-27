# Búsqueda en cuadrícula para la optimización de hiperparámetros

Utilizaremos la búsqueda en cuadrícula para explorar el espacio de hiperparámetros y encontrar los mejores hiperparámetros para nuestro modelo de SVM.

```python
# especificar los parámetros para buscar
param_grid = {
    "average": [True, False],
    "l1_ratio": np.linspace(0, 1, num=10),
    "alpha": np.power(10, np.arange(-2, 1, dtype=float)),
}

# ejecutar la búsqueda en cuadrícula
grid_search = GridSearchCV(clf, param_grid=param_grid)

start = time()
grid_search.fit(X, y)

print(
    "GridSearchCV tomó %.2f segundos para %d configuraciones de parámetros candidatas."
    % (time() - start, len(grid_search.cv_results_["params"]))
)

# imprimir los resultados
report(grid_search.cv_results_)
```
