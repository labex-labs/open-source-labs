# Ordenar una lista por índices

Escribe una función `sort_by_indexes(lst, indexes, reverse=False)` que tome dos listas como argumentos y devuelva una nueva lista ordenada según los índices de la segunda lista. La función debe tener los siguientes parámetros:

- `lst`: Una lista de elementos a ordenar.
- `indexes`: Una lista de enteros que representan los índices deseados para ordenar la `lst`.
- `reverse`: Un parámetro booleano opcional que, cuando se establece en `True`, ordena la lista en orden inverso.

La función debe devolver una nueva lista ordenada según los índices de la segunda lista.

```python
def sort_by_indexes(lst, indexes, reverse=False):
  return [val for (_, val) in sorted(zip(indexes, lst), key=lambda x: \
          x[0], reverse=reverse)]
```

```python
a = ['eggs', 'bread', 'oranges', 'jam', 'apples','milk']
b = [3, 2, 6, 4, 1, 5]
sort_by_indexes(a, b) # ['apples', 'bread', 'eggs', 'jam','milk', 'oranges']
sort_by_indexes(a, b, True)
# ['oranges','milk', 'jam', 'eggs', 'bread', 'apples']
```
