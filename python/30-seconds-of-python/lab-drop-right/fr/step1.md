# Supprimer des éléments d'une liste à partir de la droite

Écrivez une fonction `drop_right(a, n = 1)` qui prend une liste `a` et un entier optionnel `n` et renvoie une nouvelle liste avec `n` éléments supprimés de la fin droite de la liste `a`. Si `n` n'est pas fourni, la fonction devrait supprimer seulement le dernier élément de la liste.

```python
def drop_right(a, n = 1):
  return a[:-n]
```

```python
drop_right([1, 2, 3]) # [1, 2]
drop_right([1, 2, 3], 2) # [1]
drop_right([1, 2, 3], 42) # []
```
