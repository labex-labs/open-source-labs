# Filtrer les valeurs non uniques d'une liste

Écrivez une fonction Python appelée `filter_non_unique(lst)` qui prend une liste en argument et renvoie une nouvelle liste ne contenant que les valeurs uniques. Pour résoudre ce problème, vous pouvez suivre ces étapes :

1. Utilisez la méthode `collections.Counter` pour obtenir le compte de chaque valeur dans la liste.
2. Utilisez une compréhension de liste pour créer une liste ne contenant que les valeurs uniques.

```python
from collections import Counter

def filter_non_unique(lst):
  return [item for item, count in Counter(lst).items() if count == 1]
```

```python
filter_non_unique([1, 2, 2, 3, 4, 4, 5]) # [1, 3, 5]
```
