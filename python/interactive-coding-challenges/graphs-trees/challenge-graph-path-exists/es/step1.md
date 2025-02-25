# Existe un camino en el grafo

## Problema

Dado un grafo dirigido y dos nodos, escribe una función de Python para determinar si existe un camino entre los dos nodos.

## Requisitos

Para resolver este problema, debemos hacer los siguientes supuestos:

- El grafo es dirigido.
- Ya tenemos las clases Graph y Node.
- El grafo está conectado.
- Las entradas son válidas.
- La solución ajusta en memoria.

## Uso de ejemplo

Supongamos que tenemos el siguiente grafo:

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

Podemos usar la siguiente función para determinar si existe un camino entre dos nodos:

```
search_path(start=0, end=2) -> True
search_path(start=0, end=0) -> True
search_path(start=4, end=5) -> False
```

Las primeras dos llamadas a la función devuelven True porque existe un camino entre los nodos de inicio y fin. La última llamada a la función devuelve False porque no existe un camino entre los nodos de inicio y fin.
