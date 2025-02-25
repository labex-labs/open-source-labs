# Compter les éléments regroupés

Écrivez une fonction `count_by(lst, fn = lambda x: x)` qui prend une liste `lst` et une fonction `fn` en arguments. La fonction devrait regrouper les éléments de la liste sur la base de la fonction donnée et renvoyer un dictionnaire avec le compte d'éléments dans chaque groupe.

Pour résoudre ce problème, vous pouvez suivre ces étapes :

1. Initialisez un dictionnaire à l'aide de `collections.defaultdict`.
2. Utilisez `map()` pour appliquer la fonction donnée à chaque élément de la liste.
3. Itérez sur les valeurs mappées et augmentez le compte de chaque élément dans le dictionnaire.

La fonction devrait renvoyer le dictionnaire résultant.

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
