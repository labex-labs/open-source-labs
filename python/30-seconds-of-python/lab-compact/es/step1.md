# Lista Compacta

Escribe una función `compact(lst)` que tome una lista como argumento y devuelva una nueva lista con todos los valores falsos eliminados. Los valores falsos incluyen `False`, `None`, `0` y `""`.

Para resolver este problema, puedes usar la función `filter()` para filtrar los valores falsos de la lista.

```python
def compact(lst):
  return list(filter(None, lst))
```

```python
compact([0, 1, False, 2, '', 3, 'a', 's', 34]) # [ 1, 2, 3, 'a', 's', 34 ]
```
