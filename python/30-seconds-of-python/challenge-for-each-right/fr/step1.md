# Exécuter une fonction pour chaque élément de liste à l'envers

## Problème

Écrivez une fonction `for_each_right(itr, fn)` qui prend une liste `itr` et une fonction `fn` en arguments. La fonction devrait exécuter `fn` une fois pour chaque élément de `itr`, en commençant par le dernier.

## Exemple

```python
for_each_right([1, 2, 3], print) # 3 2 1
```

## Contraintes

- La fonction devrait fonctionner avec n'importe quelle liste et fonction.
- La fonction ne devrait pas modifier la liste d'origine.
