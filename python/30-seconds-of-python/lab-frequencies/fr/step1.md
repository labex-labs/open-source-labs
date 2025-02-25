# Fréquences de valeurs

Écrivez une fonction Python appelée `value_frequencies(lst)` qui prend une liste en argument et renvoie un dictionnaire dont les clés sont les valeurs uniques de la liste et les valeurs sont leurs fréquences.

Pour résoudre ce problème, vous pouvez suivre ces étapes :

1. Créez un dictionnaire vide pour stocker les fréquences de chaque élément unique.
2. Parcourez la liste et utilisez `collections.defaultdict` pour stocker les fréquences de chaque élément unique.
3. Utilisez `dict()` pour renvoyer un dictionnaire avec les éléments uniques de la liste comme clés et leurs fréquences comme valeurs.

Votre fonction devrait renvoyer le dictionnaire avec les valeurs uniques et leurs fréquences.

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
