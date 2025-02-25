# Elimina elementos de la lista desde la derecha

Escribe una función `drop_right(a, n = 1)` que tome una lista `a` y un entero opcional `n` y devuelva una nueva lista con `n` elementos eliminados del extremo derecho de la lista `a`. Si no se proporciona `n`, la función debe eliminar solo el último elemento de la lista.

```python
def drop_right(a, n = 1):
  return a[:-n]
```

```python
drop_right([1, 2, 3]) # [1, 2]
drop_right([1, 2, 3], 2) # [1]
drop_right([1, 2, 3], 42) # []
```
