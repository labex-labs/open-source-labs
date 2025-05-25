# Filtrar Valores Únicos de uma Lista

Escreva uma função Python chamada `filter_unique(lst)` que recebe uma lista como argumento e retorna uma nova lista com apenas os valores não únicos. Para resolver este problema, você pode seguir estes passos:

1.  Use `collections.Counter` para obter a contagem de cada valor na lista.
2.  Use uma compreensão de lista (list comprehension) para criar uma lista contendo apenas os valores não únicos.

Sua função deve satisfazer os seguintes requisitos:

- A função deve receber uma lista como argumento.
- A função deve retornar uma nova lista com apenas os valores não únicos.
- A função não deve modificar a lista original.
- A função deve ser _case-sensitive_ (sensível a maiúsculas e minúsculas), o que significa que 'a' e 'A' são considerados valores diferentes.

```python
def filter_unique(lst):
    # seu código aqui
```

```python
from collections import Counter

def filter_unique(lst):
  return [item for item, count in Counter(lst).items() if count > 1]
```

```python
filter_unique([1, 2, 2, 3, 4, 4, 5]) # [2, 4]
```
