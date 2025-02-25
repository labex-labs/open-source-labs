# Camino más corto en un grafo

## Problema

Dado un grafo dirigido con aristas ponderadas, encontrar el camino más corto entre dos nodos.

## Requisitos

Para resolver este problema, debemos considerar los siguientes requisitos:

- ¿Es este un grafo dirigido? - Sí
- ¿Podría el grafo tener ciclos? - Sí
  - Nota: Si la respuesta fuera no, este sería un DAG.
    - Los DAGs se pueden resolver con una [ordenación topológica](http://www.geeksforgeeks.org/shortest-path-for-directed-acyclic-graphs/)
- ¿Las aristas están ponderadas? - Sí
  - Nota: Si las aristas no estuvieran ponderadas, podríamos hacer un BFS
- ¿Todas las aristas son números no negativos? - Sí
  - Nota: Los grafos con aristas negativas se pueden resolver con Bellman-Ford
    - Los grafos con ciclos de coste negativo no tienen un camino más corto definido
- ¿Tenemos que comprobar las aristas no negativas? - No
- ¿Podemos asumir que este es un grafo conectado? - Sí
- ¿Podemos asumir que las entradas son válidas? - No
- ¿Podemos asumir que ya tenemos una clase de grafo? - Sí
- ¿Podemos asumir que ya tenemos una clase de cola de prioridad? - Sí
- ¿Podemos asumir que esto cabe en memoria? - Sí

## Ejemplo

Considere el siguiente grafo:

```txt
graph.add_edge('a', 'b', weight=5)
graph.add_edge('a', 'c', weight=3)
graph.add_edge('a', 'e', weight=2)
graph.add_edge('b', 'd', weight=2)
graph.add_edge('c', 'b', weight=1)
graph.add_edge('c', 'd', weight=1)
graph.add_edge('d', 'a', weight=1)
graph.add_edge('d', 'g', weight=2)
graph.add_edge('d', 'h', weight=1)
graph.add_edge('e', 'a', weight=1)
graph.add_edge('e', 'h', weight=4)
graph.add_edge('e', 'i', weight=7)
graph.add_edge('f', 'b', weight=3)
graph.add_edge('f', 'g', weight=1)
graph.add_edge('g', 'c', weight=3)
graph.add_edge('g', 'i', weight=2)
graph.add_edge('h', 'c', weight=2)
graph.add_edge('h', 'f', weight=2)
graph.add_edge('h', 'g', weight=2)
```

Podemos encontrar el camino más corto entre el nodo 'a' y el nodo 'i' usando la clase ShortestPath:

```txt
shortest_path = ShortestPath(graph)
result = shortest_path.find_shortest_path('a', 'i')
```

El resultado esperado es:

```txt
['a', 'c', 'd', 'g', 'i']
```

También podemos comprobar el peso del camino más corto:

```txt
self.assertEqual(shortest_path.path_weight['i'], 8)
```
