# Camino más corto en un grafo no ponderado

## Problema

Dado un grafo dirigido sin pesos en las aristas, encontrar el camino más corto entre dos nodos.

## Requisitos

Para resolver este problema, deben cumplirse los siguientes requisitos:

- El grafo es dirigido.
- El grafo es no ponderado.
- Las clases `Graph` y `Node` ya están disponibles.
- Las entradas son dos nodos.
- La salida es una lista de claves de nodos que forman el camino más corto.
- Si no hay camino, devolver `None`.
- El grafo está conectado.
- Las entradas son válidas.
- El algoritmo debe caber en memoria.

## Uso de ejemplo

Supongamos que tenemos el siguiente grafo:

```
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(0, 5)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 1)
graph.add_edge(3, 2)
graph.add_edge(3, 4)
```

Podemos encontrar el camino más corto entre dos nodos utilizando la función `search_path`:

- `search_path(start=0, end=2) -> [0, 1, 3, 2]`
- `search_path(start=0, end=0) -> [0]`
- `search_path(start=4, end=5) -> None`
