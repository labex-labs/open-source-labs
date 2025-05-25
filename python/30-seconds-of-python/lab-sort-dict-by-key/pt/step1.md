# Ordenar Dicionário por Chave

Escreva uma função `sort_dict_by_key(d, reverse=False)` que recebe um dicionário `d` e retorna um novo dicionário ordenado por chave. A função deve ter um parâmetro opcional `reverse` que, por padrão, é `False`. Se `reverse` for `True`, o dicionário deve ser ordenado em ordem inversa.

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
