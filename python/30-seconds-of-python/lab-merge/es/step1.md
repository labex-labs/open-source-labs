# Fusionar listas

Escribe una función llamada `merge(*args, fill_value=None)` que tome dos o más listas como argumentos y devuelva una lista de listas. La función debe combinar los elementos de cada una de las listas de entrada según sus posiciones. Si una lista es más corta que la lista más larga, la función debe utilizar `fill_value` para los elementos restantes. Si no se proporciona `fill_value`, debe ser el valor predeterminado `None`.

Tu tarea es implementar la función `merge()`.

```python
def merge(*args, fill_value = None):
  max_length = max([len(lst) for lst in args])
  result = []
  for i in range(max_length):
    result.append([
      args[k][i] if i < len(args[k]) else fill_value for k in range(len(args))
    ])
  return result
```

```python
merge(['a', 'b'], [1, 2], [True, False]) # [['a', 1, True], ['b', 2, False]]
merge(['a'], [1, 2], [True, False]) # [['a', 1, True], [None, 2, False]]
merge(['a'], [1, 2], [True, False], fill_value = '_')
# [['a', 1, True], ['_', 2, False]]
```
