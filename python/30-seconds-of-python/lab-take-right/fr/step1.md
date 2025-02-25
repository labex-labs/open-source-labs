# Supprimer des éléments d'une liste à partir de la fin

Écrivez une fonction `take_right(lst, n=1)` qui prend une liste `lst` et un entier optionnel `n` en arguments et renvoie une nouvelle liste avec `n` éléments supprimés de la fin de la liste. Si `n` n'est pas fourni, la fonction devrait supprimer seulement le dernier élément de la liste.

Pour résoudre ce problème, vous pouvez utiliser la notation de tranche pour créer une tranche de la liste avec `n` éléments pris à partir de la fin.

```python
def take_right(itr, n = 1):
  return itr[-n:]
```

```python
take_right([1, 2, 3], 2) # [2, 3]
take_right([1, 2, 3]) # [3]
```
