# Différence de listes basée sur une fonction

Créez une fonction appelée `difference_by(a, b, fn)` qui prend trois paramètres :

- `a` : une liste d'éléments
- `b` : une liste d'éléments
- `fn` : une fonction qui sera appliquée à chaque élément des deux listes

La fonction devrait renvoyer une liste d'éléments qui sont dans la liste `a` mais pas dans la liste `b`, après avoir appliqué la fonction `fn` fournie à chaque élément des deux listes.

Pour résoudre ce problème, vous pouvez suivre ces étapes :

1. Créez un `set`, en utilisant `map()` pour appliquer `fn` à chaque élément de `b`.
2. Utilisez une compréhension de liste en combinaison avec `fn` sur `a` pour ne conserver que les valeurs qui ne sont pas contenues dans le `set` précédemment créé, `_b`.

```python
def difference_by(a, b, fn):
  _b = set(map(fn, b))
  return [item for item in a if fn(item) not in _b]
```

```python
from math import floor

difference_by([2.1, 1.2], [2.3, 3.4], floor) # [1.2]
difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x'])
# [ { x: 2 } ]
```
