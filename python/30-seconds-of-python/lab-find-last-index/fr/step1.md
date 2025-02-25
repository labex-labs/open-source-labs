# Trouver le dernier index correspondant

Écrivez une fonction `trouver_le_dernier_index(lst, fn)` qui prend une liste `lst` et une fonction `fn` en arguments. La fonction devrait renvoyer l'index du dernier élément de `lst` pour lequel `fn` renvoie `True`. Si aucun élément ne satisfait la condition, la fonction devrait renvoyer `-1`.

```python
def trouver_le_dernier_index(lst, fn):
  return len(lst) - 1 - next(i for i, x in enumerate(lst[::-1]) if fn(x))
```

```python
trouver_le_dernier_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 2
```
