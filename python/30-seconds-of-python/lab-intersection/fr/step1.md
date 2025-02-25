# Intersection de listes

Écrivez une fonction `list_intersection(a, b)` qui prend deux listes `a` et `b` en entrée et renvoie une nouvelle liste ne contenant que les éléments présents dans `a` et `b`. Si aucun élément n'est commun, la fonction doit renvoyer une liste vide.

```python
def intersection(a, b):
  _a, _b = set(a), set(b)
  return list(_a & _b)
```

```python
intersection([1, 2, 3], [4, 3, 2]) # [2, 3]
```
