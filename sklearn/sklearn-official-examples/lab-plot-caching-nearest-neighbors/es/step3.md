# Calcular el gráfico de vecinos más cercanos

En este paso, calcularemos el gráfico de vecinos más cercanos utilizando KNeighborsTransformer.

```python
# El transformador calcula el gráfico de vecinos más cercanos utilizando el número máximo
# de vecinos necesarios en la búsqueda de cuadrícula. El modelo del clasificador filtra el
# gráfico de vecinos más cercanos según lo requerido por su propio parámetro n_neighbors.
graph_model = KNeighborsTransformer(n_neighbors=max(n_neighbors_list), mode="distance")
```
