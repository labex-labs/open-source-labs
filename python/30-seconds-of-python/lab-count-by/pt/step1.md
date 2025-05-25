# Contar Elementos Agrupados

Escreva uma função `count_by(lst, fn = lambda x: x)` que recebe uma lista `lst` e uma função `fn` como argumentos. A função deve agrupar os elementos da lista com base na função fornecida e retornar um dicionário com a contagem de elementos em cada grupo.

Para resolver este problema, você pode seguir estes passos:

1. Inicialize um dicionário usando `collections.defaultdict`.
2. Use `map()` para aplicar a função fornecida a cada elemento da lista.
3. Itere sobre os valores mapeados e aumente a contagem de cada elemento no dicionário.

A função deve retornar o dicionário resultante.

```python
from collections import defaultdict

def count_by(lst, fn = lambda x: x):
  count = defaultdict(int)
  for val in map(fn, lst):
    count[val] += 1
  return dict(count)
```

```python
from math import floor

count_by([6.1, 4.2, 6.3], floor) # {6: 2, 4: 1}
count_by(['one', 'two', 'three'], len) # {3: 2, 5: 1}
```
