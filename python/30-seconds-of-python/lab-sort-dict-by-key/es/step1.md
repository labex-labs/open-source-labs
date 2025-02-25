# Ordenar un diccionario por clave

Escribe una función `sort_dict_by_key(d, reverse=False)` que tome un diccionario `d` y devuelva un nuevo diccionario ordenado por clave. La función debe tener un parámetro opcional `reverse` que por defecto sea `False`. Si `reverse` es `True`, el diccionario debe ser ordenado en orden inverso.

```python
def sort_dict_by_key(d, reverse = False):
  return dict(sorted(d.items(), reverse = reverse))
```

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
sort_dict_by_key(d) # {'five': 5, 'four': 4, 'one': 1, 'three': 3, 'two': 2}
sort_dict_by_key(d, True)
# {'two': 2, 'three': 3, 'one': 1, 'four': 4, 'five': 5}
```
