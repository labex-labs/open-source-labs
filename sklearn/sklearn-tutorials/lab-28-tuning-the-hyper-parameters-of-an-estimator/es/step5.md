# Realizar búsqueda aleatorizada con validación cruzada

La búsqueda aleatorizada toma una muestra aleatoria de un subconjunto de la cuadrícula de parámetros y evalúa el rendimiento de cada combinación utilizando validación cruzada. Es útil cuando el espacio de parámetros es grande y no es factible realizar una búsqueda exhaustiva.

```python
# Crear una instancia de RandomizedSearchCV
random_search = RandomizedSearchCV(svc, param_grid, cv=5, n_iter=10, random_state=0)

# Ajustar los datos para realizar la búsqueda aleatorizada
random_search.fit(X, y)

# Imprimir la mejor combinación de hiperparámetros
print('Mejores hiperparámetros:', random_search.best_params_)
```
