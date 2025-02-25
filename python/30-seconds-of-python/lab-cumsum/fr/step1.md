# Liste de sommes partielles

Écrivez une fonction `partial_sum(lst)` qui prend une liste de nombres en argument et renvoie une liste de sommes partielles. Votre fonction doit effectuer les étapes suivantes :

1. Utilisez `itertools.accumulate()` pour créer la somme accumulée pour chaque élément de la liste.
2. Utilisez `list()` pour convertir le résultat en une liste.
3. Retournez la liste des sommes partielles.

```python
from itertools import accumulate

def cumsum(lst):
  return list(accumulate(lst))
```

```python
cumsum(range(0, 15, 3)) # [0, 3, 9, 18, 30]
```
