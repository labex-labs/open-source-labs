# Trouver la dernière valeur correspondante

## Problème

Écrivez une fonction `find_last(lst, fn)` qui prend une liste `lst` et une fonction de test `fn` en arguments. La fonction devrait renvoyer la valeur du dernier élément de `lst` pour lequel `fn` renvoie `True`. Si aucun élément ne satisfait la fonction de test, la fonction devrait renvoyer `None`.

Pour résoudre ce problème, vous devriez utiliser une compréhension de liste et `next()` pour itérer à travers la liste dans l'ordre inverse et renvoyer le dernier élément qui satisfait la fonction de test.

## Exemple

```python
find_last([1, 2, 3, 4], lambda n: n % 2 == 1) # 3
find_last([2, 4, 6, 8], lambda n: n % 2 == 1) # None
```

Dans le premier exemple, la fonction devrait renvoyer `3` car c'est le dernier nombre impair de la liste. Dans le second exemple, la fonction devrait renvoyer `None` car il n'y a pas de nombres impairs dans la liste.
