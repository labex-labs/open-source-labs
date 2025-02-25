# Elemento más frecuente

## Problema

Escribe una función de Python llamada `most_frequent(lst)` que tome una lista de enteros como entrada y devuelva el elemento más frecuente de la lista. Si hay múltiples elementos que aparecen el mismo número de veces y tienen la frecuencia más alta, devuelve el que aparece primero en la lista.

Para resolver este problema, puedes seguir estos pasos:

1. Utiliza `set()` para obtener los valores únicos en `lst`.
2. Utiliza `max()` para encontrar el elemento que tiene más apariciones.

Tu función debe tener la siguiente firma:

```python
def most_frequent(lst: List[int]) -> int:
```

## Ejemplo

```python
assert most_frequent([1, 2, 1, 2, 3, 2, 1, 4, 2]) == 2
assert most_frequent([1, 2, 3, 4, 5]) == 1
assert most_frequent([1, 1, 1, 1, 1]) == 1
```
