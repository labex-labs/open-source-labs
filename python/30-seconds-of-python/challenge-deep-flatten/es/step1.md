# Aplanar lista anidada

## Problema

Escribe una función `deep_flatten(lst)` que tome una lista `lst` como argumento y devuelva una nueva lista que sea la versión aplanada profundamente de `lst`. La función debe utilizar recursión y la función `isinstance()` con `collections.abc.Iterable` para comprobar si un elemento es iterable. Si un elemento es iterable, la función debe aplicar `deep_flatten()` recursivamente a ese elemento. En caso contrario, la función debe devolver una lista que contenga solo ese elemento.

## Ejemplo

```python
deep_flatten([1, [2], [[3], 4], 5]) # [1, 2, 3, 4, 5]
deep_flatten([1, [2, [3, [4]]]]) # [1, 2, 3, 4]
deep_flatten([1, 2, 3, 4]) # [1, 2, 3, 4]
deep_flatten([]) # []
```
