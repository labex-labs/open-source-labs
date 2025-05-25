# Filtrar Valores Não Únicos de uma Lista

Escreva uma função Python chamada `filter_non_unique(lst)` que recebe uma lista como argumento e retorna uma nova lista com apenas os valores únicos. Para resolver este problema, você pode seguir estes passos:

1.  Use o método `collections.Counter` para obter a contagem de cada valor na lista.
2.  Use uma compreensão de lista (list comprehension) para criar uma lista contendo apenas os valores únicos.

```python
from collections import Counter

def filter_non_unique(lst):
  return [item for item, count in Counter(lst).items() if count == 1]
```

```python
filter_non_unique([1, 2, 2, 3, 4, 4, 5]) # [1, 3, 5]
```
