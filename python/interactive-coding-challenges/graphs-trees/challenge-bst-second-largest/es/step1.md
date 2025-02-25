# El segundo nodo más grande en un árbol de búsqueda binaria

## Problema

Dado un árbol de búsqueda binaria, encontrar el segundo nodo más grande en el árbol. Si la entrada es None o un solo nodo, se debe generar una excepción.

Para resolver este problema, podemos recorrer el árbol en un orden específico y llevar un registro del segundo nodo más grande que hayamos visto hasta el momento. Podemos comenzar recorriendo el subárbol derecho del nodo raíz, y si el subárbol derecho es None, entonces el nodo más grande es el propio nodo raíz. Si el subárbol derecho no es None, podemos continuar recorriendo el subárbol derecho hasta llegar a un nodo que no tenga un hijo derecho. En este punto, el nodo más grande en el árbol es el padre de este nodo. Si este nodo padre tiene un hijo izquierdo, entonces el segundo nodo más grande es el nodo más grande en el subárbol izquierdo del nodo padre. Si el nodo padre no tiene un hijo izquierdo, entonces el segundo nodo más grande es el propio nodo padre.

## Requisitos

Los requisitos para este desafío son los siguientes:

- Si la entrada es None o un solo nodo, se debe generar una excepción.
  - La entrada None debe generar un TypeError.
  - La entrada de un solo nodo debe generar un ValueError.
- Podemos asumir que ya tenemos una clase Node con un método insert.
- Podemos asumir que este problema cabe en la memoria.

## Uso de ejemplo

A continuación se presentan algunos ejemplos de cómo usar esta función:

- None o un solo nodo -> Excepción

```txt
Entrada:
                _10_
              _/    \_
             5        15
            / \       / \
           3   8     12  20
          /     \         \
         2       4        30

Salida: 20

Entrada:
                 10
                 /
                5
               / \
              3   7
Salida: 7
```
