# Supprimer des éléments d'une liste du début

## Problème

Écrivez une fonction `drop(a, n=1)` qui prend une liste `a` et un entier optionnel `n` en arguments et renvoie une nouvelle liste avec `n` éléments supprimés du début de la liste d'origine. Si `n` n'est pas fourni, la fonction doit supprimer seulement le premier élément de la liste.

## Exemple

```python
drop([1, 2, 3]) # [2, 3]
drop([1, 2, 3], 2) # [3]
drop([1, 2, 3], 42) # []
```
