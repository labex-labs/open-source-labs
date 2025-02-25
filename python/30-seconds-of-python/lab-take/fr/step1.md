# Supprimer des éléments d'une liste

Écrivez une fonction `take(itr, n=1)` qui prend une liste `itr` et un entier `n` en arguments et renvoie une nouvelle liste avec `n` éléments supprimés du début de la liste. Si `n` est supérieur à la longueur de la liste, renvoyez la liste d'origine.

```python
def take(itr, n = 1):
  return itr[:n]
```

```python
take([1, 2, 3], 5) # [1, 2, 3]
take([1, 2, 3], 0) # []
```
