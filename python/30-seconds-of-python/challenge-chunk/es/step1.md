# Dividir una lista en trozos

## Problema

Escribe una función `chunk(lst, size)` que tome una lista `lst` y un entero positivo `size` como argumentos y devuelva una lista de listas más pequeñas, cada una de las cuales tiene un tamaño máximo de `size`. Si la longitud de `lst` no es divisible uniformemente por `size`, la última lista en la lista devuelta debe contener los elementos restantes.

## Ejemplo

```python
chunk([1, 2, 3, 4, 5], 2) # [[1, 2], [3, 4], [5]]
chunk([1, 2, 3, 4, 5], 3) # [[1, 2, 3], [4, 5]]
chunk([1, 2, 3, 4, 5], 1) # [[1], [2], [3], [4], [5]]
```
