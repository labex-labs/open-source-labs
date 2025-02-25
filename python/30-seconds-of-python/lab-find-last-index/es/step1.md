# Encuentra el último índice coincidente

Escribe una función `find_last_index(lst, fn)` que tome una lista `lst` y una función `fn` como argumentos. La función debe devolver el índice del último elemento en `lst` para el cual `fn` devuelva `True`. Si ningún elemento satisface la condición, la función debe devolver `-1`.

```python
def find_last_index(lst, fn):
  return len(lst) - 1 - next(i for i, x in enumerate(lst[::-1]) if fn(x))
```

```python
find_last_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 2
```
