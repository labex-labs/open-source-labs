# Trouver l'index correspondant

Écrivez une fonction `find_index(lst, fn)` qui prend une liste `lst` et une fonction de test `fn` en arguments. La fonction devrait renvoyer l'index du premier élément de `lst` pour lequel `fn` renvoie `True`.

```python
def find_index(lst, fn):
  return next(i for i, x in enumerate(lst) if fn(x))
```

```python
find_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 0
```
