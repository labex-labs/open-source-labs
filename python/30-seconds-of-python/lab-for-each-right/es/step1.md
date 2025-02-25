# Ejecutar función para cada elemento de la lista en orden inverso

Escribe una función `for_each_right(itr, fn)` que tome una lista `itr` y una función `fn` como argumentos. La función debe ejecutar `fn` una vez para cada elemento en `itr`, comenzando desde el último.

```python
def for_each_right(itr, fn):
  for el in itr[::-1]:
    fn(el)
```

```python
for_each_right([1, 2, 3], print) # 3 2 1
```
