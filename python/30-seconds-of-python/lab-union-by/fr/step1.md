# Union de listes basée sur une fonction

Écrivez une fonction `union_by(a, b, fn)` qui prend deux listes `a` et `b` et une fonction `fn`. La fonction devrait renvoyer une liste qui contient chaque élément qui existe dans l'une ou l'autre des deux listes une fois, après avoir appliqué la fonction fournie à chaque élément des deux.

Pour résoudre ce problème, vous pouvez suivre les étapes suivantes :

1. Créez un `ensemble` en appliquant `fn` à chaque élément de `a`.
2. Utilisez une compréhension de liste en combinaison avec `fn` sur `b` pour ne conserver que les valeurs qui ne sont pas contenues dans l'ensemble précédemment créé, `_a`.
3. Enfin, créez un `ensemble` à partir du résultat précédent et `a` et convertissez-le en `liste`.

La fonction devrait avoir les paramètres d'entrée suivants :

- `a` : une liste d'éléments
- `b` : une liste d'éléments
- `fn` : une fonction qui prend un élément et renvoie une valeur

La fonction devrait renvoyer une liste d'éléments.

```python
def union_by(a, b, fn):
  _a = set(map(fn, a))
  return list(set(a + [item for item in b if fn(item) not in _a]))
```

```python
from math import floor

union_by([2.1], [1.2, 2.3], floor) # [2.1, 1.2]
```
