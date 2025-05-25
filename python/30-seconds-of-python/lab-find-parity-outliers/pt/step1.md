# Encontrar _Outliers_ de Paridade

Escreva uma função `find_parity_outliers(nums)` que recebe uma lista de inteiros `nums` como argumento e retorna uma lista de todos os _outliers_ de paridade em `nums`.

Para resolver este problema, você pode seguir estes passos:

1. Use `collections.Counter` com uma _list comprehension_ para contar os valores pares e ímpares na lista.
2. Use `collections.Counter.most_common()` para obter a paridade mais comum.
3. Use uma _list comprehension_ para encontrar todos os elementos que não correspondem à paridade mais comum.

```python
from collections import Counter

def find_parity_outliers(nums):
  return [
    x for x in nums
    if x % 2 != Counter([n % 2 for n in nums]).most_common()[0][0]
  ]
```

```python
find_parity_outliers([1, 2, 3, 4, 6]) # [1, 3]
```
