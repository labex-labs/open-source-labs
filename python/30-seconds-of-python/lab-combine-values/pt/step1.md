# Combinar Valores de Dicionário

Escreva uma função `combine_values(*dicts)` que recebe dois ou mais dicionários como argumentos e retorna um novo dicionário que combina os valores dos dicionários de entrada. A função deve realizar os seguintes passos:

1.  Crie um novo `collections.defaultdict` com `list` como o valor padrão para cada chave.
2.  Itere sobre os dicionários de entrada e, para cada dicionário:
    - Itere sobre as chaves do dicionário.
    - Anexe o valor da chave à lista de valores para essa chave no `defaultdict`.
3.  Converta o `defaultdict` em um dicionário regular usando a função `dict()`.
4.  Retorne o dicionário resultante.

A função deve ter a seguinte assinatura:

```python
def combine_values(*dicts):
    pass
```

```python
from collections import defaultdict

def combine_values(*dicts):
  res = defaultdict(list)
  for d in dicts:
    for key in d:
      res[key].append(d[key])
  return dict(res)
```

```python
d1 = {'a': 1, 'b': 'foo', 'c': 400}
d2 = {'a': 3, 'b': 200, 'd': 400}

combine_values(d1, d2) # {'a': [1, 3], 'b': ['foo', 200], 'c': [400], 'd': [400]}
```
