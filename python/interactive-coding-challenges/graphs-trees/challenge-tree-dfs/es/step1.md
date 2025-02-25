# Búsqueda en profundidad en árboles

## Problema

Implementar recorridos en profundidad (en orden, pre-orden, post-orden) en un árbol binario. Para el recorrido en orden, visitamos el subárbol izquierdo, luego el nodo actual y luego el subárbol derecho. Para el recorrido en pre-orden, visitamos el nodo actual, luego el subárbol izquierdo y luego el subárbol derecho. Para el recorrido en post-orden, visitamos el subárbol izquierdo, luego el subárbol derecho y luego el nodo actual.

## Requisitos

Para completar este desafío, debemos cumplir con los siguientes requisitos:

- Podemos asumir que ya tenemos una clase `Node` con un método `insert`.
- Cuando procesamos cada nodo, debemos llamar a un método de entrada `visit_func` en el nodo.
- Podemos asumir que esto cabe en memoria.

## Uso de ejemplo

A continuación se presentan algunos ejemplos de cómo usar el algoritmo de búsqueda en profundidad:

### Recorrido en orden

Para un árbol binario con valores 5, 2, 8, 1 y 3, el recorrido en orden sería 1, 2, 3, 5 y 8. Para un árbol binario con valores 1, 2, 3, 4 y 5, el recorrido en orden sería 1, 2, 3, 4 y 5.

### Recorrido en pre-orden

Para un árbol binario con valores 5, 2, 8, 1 y 3, el recorrido en pre-orden sería 5, 2, 1, 3 y 8. Para un árbol binario con valores 1, 2, 3, 4 y 5, el recorrido en pre-orden sería 1, 2, 3, 4 y 5.

### Recorrido en post-orden

Para un árbol binario con valores 5, 2, 8, 1 y 3, el recorrido en post-orden sería 1, 3, 2, 8 y 5. Para un árbol binario con valores 1, 2, 3, 4 y 5, el recorrido en post-orden sería 5, 4, 3, 2 y 1.
