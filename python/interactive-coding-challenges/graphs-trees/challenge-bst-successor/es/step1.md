# Sucesor en un BST

## Problema

Dado un árbol de búsqueda binaria y un nodo en él, encontrar el sucesor en orden de ese nodo. El sucesor de un nodo es el nodo que aparece inmediatamente después del nodo dado en un recorrido en orden del árbol. Si no hay sucesor, devolver `None`. Si la entrada es `None`, lanzar una excepción. Podemos suponer que ya tenemos una clase `Node` que lleva un registro de los padres, y podemos suponer que esto cabe en memoria.

## Requisitos

- La función debe devolver el sucesor en orden de un nodo dado en un árbol de búsqueda binaria.
- Si no hay sucesor, la función debe devolver `None`.
- Si la entrada es `None`, la función debe lanzar una excepción.
- Podemos suponer que ya tenemos una clase `Node` que lleva un registro de los padres.
- Podemos suponer que esto cabe en memoria.

## Uso de ejemplo

```txt
          _5_
        /     \
       3       8
      / \    /   \
     2   4  6    12
    /        \   / \
   1          7 10  15
               /
              9

Entrada: None  Salida: Excepción
Entrada: 4     Salida: 5
Entrada: 5     Salida: 6
Entrada: 8     Salida: 9
Entrada: 15    Salida: None
```
