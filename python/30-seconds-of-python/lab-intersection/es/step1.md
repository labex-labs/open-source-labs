# Intersección de listas

Escribe una función `list_intersection(a, b)` que tome dos listas `a` y `b` como entrada y devuelva una nueva lista que contenga solo los elementos que están presentes en ambas `a` y `b`. Si no hay elementos comunes, la función debe devolver una lista vacía.

```python
def intersection(a, b):
  _a, _b = set(a), set(b)
  return list(_a & _b)
```

```python
intersection([1, 2, 3], [4, 3, 2]) # [2, 3]
```
