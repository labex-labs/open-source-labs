# Encuentra el índice coincidente

Escribe una función `find_index(lst, fn)` que tome una lista `lst` y una función de prueba `fn` como argumentos. La función debe devolver el índice del primer elemento en `lst` para el cual `fn` devuelva `True`.

```python
def find_index(lst, fn):
  return next(i for i, x in enumerate(lst) if fn(x))
```

```python
find_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 0
```
