# Ordenamiento por selección

## Problema

Implementar el ordenamiento por selección en Python. El algoritmo debe tomar una lista de enteros como entrada y devolver la lista ordenada. El algoritmo debe funcionar de la siguiente manera:

1. Encontrar el elemento mínimo en la parte no ordenada de la lista.
2. Intercambiarlo con el primer elemento de la parte no ordenada de la lista.
3. Mover el límite de la parte ordenada de la lista un elemento hacia la derecha.

Repetir los pasos 1-3 hasta que toda la lista esté ordenada.

## Requisitos

Para implementar el ordenamiento por selección en Python, deben cumplirse los siguientes requisitos:

- El algoritmo debe tomar una lista de enteros como entrada.
- El algoritmo debe devolver una lista de enteros ordenada.
- El algoritmo debe implementarse utilizando el algoritmo de ordenamiento por selección.
- El algoritmo debe funcionar para listas de cualquier longitud.
- El algoritmo debe manejar los elementos duplicados en la lista.
- La lista de entrada puede no estar ordenada.
- La lista de entrada puede contener datos no válidos, como valores no enteros.
- El algoritmo debe ser eficiente en memoria y no utilizar demasiada memoria.

## Uso de ejemplo

Los siguientes ejemplos demuestran el uso del algoritmo de ordenamiento por selección:

- `selection_sort([])` devuelve `[]`
- `selection_sort([1])` devuelve `[1]`
- `selection_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])` devuelve `[1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]`
