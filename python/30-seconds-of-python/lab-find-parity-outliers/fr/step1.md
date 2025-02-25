# Trouver les anomalies de parité

Écrivez une fonction `find_parity_outliers(nums)` qui prend une liste d'entiers `nums` en argument et renvoie une liste de tous les anomalies de parité dans `nums`.

Pour résoudre ce problème, vous pouvez suivre ces étapes :

1. Utilisez `collections.Counter` avec une compréhension de liste pour compter les valeurs paires et impaires dans la liste.
2. Utilisez `collections.Counter.most_common()` pour obtenir la parité la plus commune.
3. Utilisez une compréhension de liste pour trouver tous les éléments qui ne correspondent pas à la parité la plus commune.

```python
from collections import Counter

def find_parity_outliers(nums):
  return [
    x for x in nums
    if x % 2!= Counter([n % 2 for n in nums]).most_common()[0][0]
  ]
```

```python
find_parity_outliers([1, 2, 3, 4, 6]) # [1, 3]
```
