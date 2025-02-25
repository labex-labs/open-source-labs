# Décaler des éléments d'une liste

Écrivez une fonction `offset(lst, offset)` qui prend une liste `lst` et un entier `offset` en arguments et renvoie une nouvelle liste avec la quantité spécifiée d'éléments déplacés à la fin de la liste. Si l'`offset` est positif, déplacez les premiers `offset` éléments à la fin de la liste. Si l'`offset` est négatif, déplacez les derniers `offset` éléments au début de la liste.

```python
def offset(lst, offset):
  return lst[offset:] + lst[:offset]
```

```python
offset([1, 2, 3, 4, 5], 2) # [3, 4, 5, 1, 2]
offset([1, 2, 3, 4, 5], -2) # [4, 5, 1, 2, 3]
```
