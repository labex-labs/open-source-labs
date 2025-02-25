# Contenido de listas

## Problema

Escribe una función `is_contained_in(a, b)` que tome dos listas como argumentos y devuelva `True` si todos los elementos de la lista `a` están contenidos en la lista `b`, independientemente del orden. En caso contrario, la función debe devolver `False`.

Para resolver este problema, puedes utilizar el siguiente enfoque:

1. Recorre cada valor único en la lista `a`.
2. Para cada valor, comprueba si aparece más veces en la lista `a` que en la lista `b`.
3. Si algún valor aparece más veces en la lista `a` que en la lista `b`, devuelve `False`.
4. Si todos los valores de la lista `a` aparecen en la lista `b` al menos tantas veces como aparecen en la lista `a`, devuelve `True`.

## Ejemplo

```python
assert is_contained_in([1, 4], [2, 4, 1]) == True
assert is_contained_in([1, 2, 3], [3, 2, 1]) == True
assert is_contained_in([1, 2, 3], [3, 2, 2, 1]) == False
assert is_contained_in([1, 2, 3], [4, 5, 6]) == False
```
