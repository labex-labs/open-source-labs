# Determinar los nodos comunes para un grupo de muestras

Para un grupo de muestras, podemos determinar los nodos comunes por los que pasan las muestras utilizando el método `decision_path` y el método `toarray` para convertir la matriz de indicadores en una matriz densa.

```python
sample_ids = [0, 1]
# matriz booleana que indica los nodos por los que pasan ambas muestras
common_nodes = node_indicator.toarray()[sample_ids].sum(axis=0) == len(sample_ids)
# obtener los ids de los nodos utilizando su posición en la matriz
common_node_id = np.arange(n_nodes)[common_nodes]

print(
    "\nLas siguientes muestras {samples} comparten el nodo(s) {nodes} en el árbol.".format(
        samples=sample_ids, nodes=common_node_id
    )
)
print("Esto es el {prop}% de todos los nodos.".format(prop=100 * len(common_node_id) / n_nodes))
```
