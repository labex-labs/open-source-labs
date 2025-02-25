# Trouver tous les index correspondants

## Problème

Écrivez une fonction `trouver_index_de_tous(lst, fn)` qui prend une liste `lst` et une fonction de test `fn` en arguments et renvoie une liste d'index de tous les éléments de `lst` pour lesquels `fn` renvoie `True`.

### Entrée

- Une liste `lst` d'entiers.
- Une fonction de test `fn` qui prend un entier en entrée et renvoie une valeur booléenne.

### Sortie

- Une liste d'entiers représentant les index de tous les éléments de `lst` pour lesquels `fn` renvoie `True`.

## Exemple

```python
trouver_index_de_tous([1, 2, 3, 4], lambda n: n % 2 == 1) # [0, 2]
trouver_index_de_tous([1, 2, 3, 4], lambda n: n > 2) # [2, 3]
trouver_index_de_tous([1, 2, 3, 4], lambda n: n < 0) # []
```

### Note

- Dans le premier exemple, la fonction de test `lambda n: n % 2 == 1` vérifie si l'entier est impair. La fonction renvoie `[0, 2]` car les éléments aux index `0` et `2` de la liste `[1, 2, 3, 4]` sont impairs.
- Dans le second exemple, la fonction de test `lambda n: n > 2` vérifie si l'entier est supérieur à `2`. La fonction renvoie `[2, 3]` car les éléments aux index `2` et `3` de la liste `[1, 2, 3, 4]` sont supérieurs à `2`.
- Dans le troisième exemple, la fonction de test `lambda n: n < 0` vérifie si l'entier est négatif. La fonction renvoie `[]` car il n'y a pas d'éléments négatifs dans la liste `[1, 2, 3, 4]`.
