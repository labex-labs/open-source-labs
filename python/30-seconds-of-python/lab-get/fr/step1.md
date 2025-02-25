# Récupérer une valeur imbriquée

Écrivez une fonction `get(d, selecteurs)` qui prend un dictionnaire ou une liste `d` et une liste de sélecteurs `selecteurs` en arguments et renvoie la valeur de la clé imbriquée indiquée par la liste de sélecteurs donnée. Si la clé n'existe pas, renvoyez `None`.

Pour implémenter cette fonction, utilisez `functools.reduce()` pour itérer sur la liste `selecteurs`. Appliquez `operator.getitem()` pour chaque clé dans `selecteurs`, en récupérant la valeur à utiliser comme itérable pour l'itération suivante.

```python
from functools import reduce
from operator import getitem

def get(d, selecteurs):
  return reduce(getitem, selecteurs, d)
```

```python
users = {
  'freddy': {
    'name': {
      'first': 'fred',
      'last': 'smith'
    },
    'postIds': [1, 2, 3]
  }
}
get(users, ['freddy', 'name', 'last']) # 'smith'
get(users, ['freddy', 'postIds', 1]) # 2
```
