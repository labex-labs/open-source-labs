# Lista de sumas parciales

## Problema

Escribe una función `partial_sum(lst)` que tome una lista de números como argumento y devuelva una lista de sumas parciales. Tu función debe realizar los siguientes pasos:

1. Utiliza `itertools.accumulate()` para crear la suma acumulada para cada elemento de la lista.
2. Utiliza `list()` para convertir el resultado en una lista.
3. Devuelve la lista de sumas parciales.

## Ejemplo

```python
partial_sum([1, 2, 3, 4, 5]) # [1, 3, 6, 10, 15]
partial_sum([2, 4, 6, 8, 10]) # [2, 6, 12, 20, 30]
partial_sum([5, 10, 15, 20, 25]) # [5, 15, 30, 50, 75]
```
