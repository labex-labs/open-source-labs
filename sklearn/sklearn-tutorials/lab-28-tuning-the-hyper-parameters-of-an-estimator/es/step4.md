# Realizar búsqueda en cuadrícula con validación cruzada

La búsqueda en cuadrícula explora exhaustivamente todas las combinaciones posibles de hiperparámetros en la cuadrícula de parámetros especificada. Evalúa el rendimiento de cada combinación utilizando validación cruzada.

```python
# Crear una instancia de GridSearchCV
grid_search = GridSearchCV(svc, param_grid, cv=5)

# Ajustar los datos para realizar la búsqueda en cuadrícula
grid_search.fit(X, y)

# Imprimir la mejor combinación de hiperparámetros
print('Mejores hiperparámetros:', grid_search.best_params_)
```
