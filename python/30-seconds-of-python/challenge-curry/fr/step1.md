# Fonction Curry

## Problème

Écrire une fonction `curry(fn, *args)` qui curry une fonction donnée `fn`. La fonction devrait retourner une nouvelle fonction qui se comporte comme `fn` avec les arguments donnés, `args`, partiellement appliqués.

## Exemple

```python
add = lambda x, y: x + y
add10 = curry(add, 10)
add10(20) # 30
```
