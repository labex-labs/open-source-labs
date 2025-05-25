# Ordenar Lista por Índices

Escreva uma função `sort_by_indexes(lst, indexes, reverse=False)` que recebe duas listas como argumentos e retorna uma nova lista ordenada com base nos índices da segunda lista. A função deve ter os seguintes parâmetros:

- `lst`: Uma lista de elementos a serem ordenados.
- `indexes`: Uma lista de inteiros representando os índices desejados para ordenar a `lst`.
- `reverse`: Um parâmetro booleano opcional que, quando definido como `True`, ordena a lista em ordem inversa.

A função deve retornar uma nova lista ordenada com base nos índices da segunda lista.

```python
def sort_by_indexes(lst, indexes, reverse=False):
  return [val for (_, val) in sorted(zip(indexes, lst), key=lambda x: \
          x[0], reverse=reverse)]
```

```python
a = ['eggs', 'bread', 'oranges', 'jam', 'apples', 'milk']
b = [3, 2, 6, 4, 1, 5]
sort_by_indexes(a, b) # ['apples', 'bread', 'eggs', 'jam', 'milk', 'oranges']
sort_by_indexes(a, b, True)
# ['oranges', 'milk', 'jam', 'eggs', 'bread', 'apples']
```
