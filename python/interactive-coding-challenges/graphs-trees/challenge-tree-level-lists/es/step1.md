# Listas por Nivel del Árbol

## Problema

Dado un árbol de búsqueda binaria, crear una lista para cada nivel del árbol. Cada lista debe contener los nodos del nivel correspondiente del árbol. Las listas deben devolverse en una matriz de matrices, donde cada submatriz representa un nivel del árbol.

## Requisitos

Para resolver este problema, deben cumplirse los siguientes requisitos:

- El árbol dado es un árbol de búsqueda binaria.
- Cada nivel del árbol debe representarse por una lista de nodos.
- Ya se ha proporcionado una clase Nodo con un método insertar.
- La solución debe caber en memoria.

## Uso de Ejemplo

Por ejemplo, dado el árbol de búsqueda binaria con los siguientes valores:

```
5, 3, 8, 2, 4, 1, 7, 6, 9, 10, 11
```

La función debe devolver la siguiente matriz de matrices:

```
[[5], [3, 8], [2, 4, 7, 9], [1, 6, 10], [11]]
```

Tenga en cuenta que cada número en el resultado es en realidad un nodo que contiene el número.
