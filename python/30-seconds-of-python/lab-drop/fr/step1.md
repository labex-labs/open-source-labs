# Supprimer des éléments d'une liste du début

Écrivez une fonction `drop(a, n=1)` qui prend une liste `a` et un entier optionnel `n` en arguments et renvoie une nouvelle liste avec `n` éléments supprimés du début de la liste d'origine. Si `n` n'est pas fourni, la fonction devrait supprimer seulement le premier élément de la liste.

```python
def drop(a, n = 1):
  return a[n:]
```

```python
drop([1, 2, 3]) # [2, 3]
drop([1, 2, 3], 2) # [3]
drop([1, 2, 3], 42) # []
```
