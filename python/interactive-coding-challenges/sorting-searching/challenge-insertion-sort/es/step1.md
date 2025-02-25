# Clasificación por inserción

## Problema

El problema es implementar la clasificación por inserción en Python. Dada una lista no ordenada de elementos, el algoritmo debe ordenar la lista en orden ascendente. El algoritmo funciona iterando sobre la lista e insertando cada elemento en su posición correcta en la parte ordenada de la lista.

El algoritmo comienza asumiendo que el primer elemento de la lista ya está ordenado. Luego itera sobre los elementos restantes de la lista, comparando cada elemento con los elementos de la parte ordenada de la lista. Si el elemento es más pequeño que el elemento actual en la parte ordenada de la lista, se inserta antes de ese elemento. Si el elemento es más grande que todos los elementos de la parte ordenada de la lista, se inserta al final de la parte ordenada de la lista.

## Requisitos

Para implementar la clasificación por inserción en Python, se deben cumplir los siguientes requisitos:

- Una solución simple es suficiente.
- Se permiten duplicados.
- La entrada no necesariamente es válida, por lo que el algoritmo debe manejar la entrada no válida de manera adecuada.
- El algoritmo debe caber en memoria.

## Uso de ejemplo

Los siguientes son algunos ejemplos de cómo usar el algoritmo de clasificación por inserción:

- Ninguno -> Excepción: Si la entrada es None, se debe generar una excepción.
- Entrada vacía -> []: Si la entrada es una lista vacía, la salida también debe ser una lista vacía.
- Un solo elemento -> [elemento]: Si la entrada es una lista con un solo elemento, la salida debe ser la misma lista.
- Dos o más elementos: Si la entrada es una lista con dos o más elementos, la salida debe ser una lista ordenada en orden ascendente.
