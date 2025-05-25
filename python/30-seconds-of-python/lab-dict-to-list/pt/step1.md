# Dicionário para Lista

Escreva uma função `dict_to_list(d)` que recebe um dicionário `d` como argumento e retorna uma lista de tuplas. Cada tupla deve conter um par chave-valor do dicionário. A ordem das tuplas na lista deve ser a mesma ordem dos pares chave-valor no dicionário.

```python
def dict_to_list(d):
  return list(d.items())
```

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
dict_to_list(d)
# [('one', 1), ('three', 3), ('five', 5), ('two', 2), ('four', 4)]
```
