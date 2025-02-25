# Ejecutar una función para cada elemento de una lista

Escribe una función `for_each(itr, fn)` que tome una lista `itr` y una función `fn` como argumentos. La función debe ejecutar `fn` una vez para cada elemento en `itr`.

```python
def for_each(itr, fn):
  for el in itr:
    fn(el)
```

```python
for_each([1, 2, 3], print) # 1 2 3
```
