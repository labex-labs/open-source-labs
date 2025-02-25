# Intersection de listes basée sur une fonction

Écrivez une fonction `intersection_by(a, b, fn)` qui prend deux listes `a` et `b`, et une fonction `fn`. La fonction devrait renvoyer une liste d'éléments qui existent dans les deux listes, après avoir appliqué la fonction fournie à chaque élément des deux listes.

### Entrée

- Deux listes `a` et `b` (1 <= len(a), len(b) <= 1000)
- Une fonction `fn` qui prend un argument et renvoie une valeur

### Sortie

- Une liste d'éléments qui existent dans les deux listes, après avoir appliqué la fonction fournie à chaque élément des deux listes.

```python
def intersection_by(a, b, fn):
  _b = set(map(fn, b))
  return [item for item in a if fn(item) in _b]
```

```python
from math import floor

intersection_by([2.1, 1.2], [2.3, 3.4], floor) # [2.1]
```
