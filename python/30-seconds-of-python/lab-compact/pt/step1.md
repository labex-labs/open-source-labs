# Lista Compacta

Escreva uma função `compact(lst)` que recebe uma lista como argumento e retorna uma nova lista com todos os valores falsos removidos. Valores falsos incluem `False`, `None`, `0` e `""`.

Para resolver este problema, você pode usar a função `filter()` para filtrar os valores falsos da lista.

```python
def compact(lst):
  return list(filter(None, lst))
```

```python
compact([0, 1, False, 2, '', 3, 'a', 's', 34]) # [ 1, 2, 3, 'a', 's', 34 ]
```
