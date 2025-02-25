# Encuentra el último valor coincidente

Escribe una función `find_last(lst, fn)` que tome una lista `lst` y una función de prueba `fn` como argumentos. La función debe devolver el valor del último elemento en `lst` para el cual `fn` devuelva `True`. Si ningún elemento satisface la función de prueba, la función debe devolver `None`.

Para resolver este problema, debes usar una comprensión de listas y `next()` para iterar a través de la lista en orden inverso y devolver el último elemento que satisface la función de prueba.

```python
def find_last(lst, fn):
  return next(x for x in lst[::-1] if fn(x))
```

```python
find_last([1, 2, 3, 4], lambda n: n % 2 == 1) # 3
```
