# Trouver l'index correspondant

## Problème

Écrivez une fonction `trouver_index(lst, fn)` qui prend une liste `lst` et une fonction de test `fn` en arguments. La fonction devrait renvoyer l'index du premier élément de `lst` pour lequel `fn` renvoie `True`.

## Exemple

```python
trouver_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 0
```
