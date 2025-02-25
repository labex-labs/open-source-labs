# Trouver la valeur correspondante

## Problème

Écrivez une fonction appelée `find(lst, fn)` qui prend une liste `lst` et une fonction de test `fn` en arguments. La fonction devrait renvoyer la valeur du premier élément de `lst` pour lequel `fn` renvoie `True`. Si aucun élément ne satisfait la fonction de test, la fonction devrait renvoyer `None`.

## Exemple

```python
find([1, 2, 3, 4], lambda n: n % 2 == 1) # 1
find(['apple', 'banana', 'cherry'], lambda s: s.startswith('b')) # 'banana'
find([2, 4, 6, 8], lambda n: n % 2 == 1) # None
```
