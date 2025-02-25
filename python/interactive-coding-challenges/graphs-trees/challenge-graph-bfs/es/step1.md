# Búsqueda en anchura en grafos

## Problema

Implementar la búsqueda en anchura en un grafo implica visitar todos los vértices del grafo en orden de búsqueda en anchura, comenzando desde un vértice fuente dado. El algoritmo funciona visitando el vértice fuente, luego visitando todos sus vecinos, luego visitando todos los vecinos de sus vecinos, y así sucesivamente. El orden en el que se visitan los vértices es importante, ya que determina el camino más corto desde el vértice fuente hasta todos los demás vértices del grafo.

## Requisitos

Para implementar la búsqueda en anchura en un grafo, deben cumplirse los siguientes requisitos:

- El grafo es dirigido.
- Las clases `Graph` y `Node` ya están disponibles.
- El grafo está conectado.
- Las entradas son válidas.
- El algoritmo cabe en la memoria.

## Uso de ejemplo

Supongamos que tenemos un grafo con las siguientes aristas:

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

Si comenzamos la búsqueda en anchura desde el vértice 0, el orden en que se visitan los nodos será [0, 1, 4, 5, 3, 2]. Esto significa que el vértice 0 se visita primero, seguido de sus vecinos 1, 4 y 5, luego los vecinos de 1 (3 y 4), y luego el vecino de 3 (2).
