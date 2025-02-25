# Búsqueda en profundidad (DFS) en Grafos

## Problema

Implementar la búsqueda en profundidad en un grafo dirigido. El algoritmo debe comenzar en un nodo dado y visitar todos los nodos alcanzables en el grafo. El orden en el que se visitan los nodos debe ser registrado y devuelto como una lista.

## Requisitos

Para implementar la DFS en un grafo dirigido, deben cumplirse los siguientes requisitos:

- El grafo es dirigido.
- Las clases Grafo y Nodo ya están implementadas.
- El grafo está conectado.
- Las entradas son válidas.
- El algoritmo ajusta en memoria.

## Uso de ejemplo

Supongamos que tenemos un grafo dirigido con las siguientes aristas:

```
graph.add_edge(0, 1, 5)
graph.add_edge(0, 4, 3)
graph.add_edge(0, 5, 2)
graph.add_edge(1, 3, 5)
graph.add_edge(1, 4, 4)
graph.add_edge(2, 1, 6)
graph.add_edge(3, 2, 7)
graph.add_edge(3, 4, 8)
```

Si comenzamos la DFS en el nodo 0, el orden de los nodos visitados debe ser [0, 1, 3, 2, 4, 5].
