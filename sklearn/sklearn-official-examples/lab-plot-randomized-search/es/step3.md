# Búsqueda aleatorizada para la optimización de hiperparámetros

Utilizaremos la búsqueda aleatorizada para explorar el espacio de hiperparámetros y encontrar los mejores hiperparámetros para nuestro modelo de SVM.

```python
# especificar los parámetros y las distribuciones para muestrear
param_dist = {
    "average": [True, False],
    "l1_ratio": stats.uniform(0, 1),
    "alpha": stats.loguniform(1e-2, 1e0),
}

# ejecutar la búsqueda aleatorizada
n_iter_search = 15
random_search = RandomizedSearchCV(
    clf, param_distributions=param_dist, n_iter=n_iter_search
)

start = time()
random_search.fit(X, y)
print(
    "RandomizedSearchCV tomó %.2f segundos para %d configuraciones de parámetros candidatas."
    % ((time() - start), n_iter_search)
)

# imprimir los resultados
report(random_search.cv_results_)
```
