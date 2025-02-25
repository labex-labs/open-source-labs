# Encontrar el valor coincidente

Escribe una función llamada `find(lst, fn)` que tome una lista `lst` y una función de prueba `fn` como argumentos. La función debe devolver el valor del primer elemento en `lst` para el cual `fn` devuelva `True`. Si ningún elemento satisface la función de prueba, la función debe devolver `None`.

```python
def find(lst, fn):
  return next(x for x in lst if fn(x))
```

```python
find([1, 2, 3, 4], lambda n: n % 2 == 1) # 1
```
