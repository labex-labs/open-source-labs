# Trouver la valeur correspondante

Écrivez une fonction appelée `find(lst, fn)` qui prend une liste `lst` et une fonction de test `fn` en arguments. La fonction devrait renvoyer la valeur du premier élément de `lst` pour lequel `fn` renvoie `True`. Si aucun élément ne satisfait à la fonction de test, la fonction devrait renvoyer `None`.

```python
def find(lst, fn):
  return next(x for x in lst if fn(x))
```

```python
find([1, 2, 3, 4], lambda n: n % 2 == 1) # 1
```
