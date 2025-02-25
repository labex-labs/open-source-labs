# Trouver la dernière valeur correspondante

Écrivez une fonction `trouver_dernier(lst, fn)` qui prend une liste `lst` et une fonction de test `fn` en arguments. La fonction devrait renvoyer la valeur du dernier élément de `lst` pour lequel `fn` renvoie `True`. Si aucun élément ne satisfait la fonction de test, la fonction devrait renvoyer `None`.

Pour résoudre ce problème, vous devriez utiliser une compréhension de liste et `next()` pour itérer à travers la liste dans l'ordre inverse et renvoyer le dernier élément qui satisfait la fonction de test.

```python
def trouver_dernier(lst, fn):
  return next(x for x in lst[::-1] if fn(x))
```

```python
trouver_dernier([1, 2, 3, 4], lambda n: n % 2 == 1) # 3
```
