# Frequências de Valores

Escreva uma função Python chamada `value_frequencies(lst)` que recebe uma lista como argumento e retorna um dicionário com os valores únicos da lista como chaves e suas frequências como valores.

Para resolver este problema, você pode seguir estes passos:

1.  Crie um dicionário vazio para armazenar as frequências de cada elemento único.
2.  Itere pela lista e use `collections.defaultdict` para armazenar as frequências de cada elemento único.
3.  Use `dict()` para retornar um dicionário com os elementos únicos da lista como chaves e suas frequências como valores.

Sua função deve retornar o dicionário com os valores únicos e suas frequências.

```python
from collections import defaultdict

def frequencies(lst):
  freq = defaultdict(int)
  for val in lst:
    freq[val] += 1
  return dict(freq)
```

```python
frequencies(['a', 'b', 'a', 'c', 'a', 'a', 'b']) # { 'a': 4, 'b': 2, 'c': 1 }
```
