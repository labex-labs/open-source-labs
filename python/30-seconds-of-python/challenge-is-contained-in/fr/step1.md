# Contenu de liste

## Problème

Écrivez une fonction `is_contained_in(a, b)` qui prend deux listes en arguments et renvoie `True` si tous les éléments de la liste `a` sont contenus dans la liste `b`, quelle que soit l'ordre. Sinon, la fonction devrait renvoyer `False`.

Pour résoudre ce problème, vous pouvez utiliser l'approche suivante :

1. Parcourez chaque valeur unique dans la liste `a`.
2. Pour chaque valeur, vérifiez si elle apparaît plus de fois dans la liste `a` que dans la liste `b`.
3. Si une valeur apparaît plus de fois dans la liste `a` que dans la liste `b`, renvoyez `False`.
4. Si toutes les valeurs de la liste `a` apparaissent dans la liste `b` au moins autant de fois qu'elles apparaissent dans la liste `a`, renvoyez `True`.

## Exemple

```python
assert is_contained_in([1, 4], [2, 4, 1]) == True
assert is_contained_in([1, 2, 3], [3, 2, 1]) == True
assert is_contained_in([1, 2, 3], [3, 2, 2, 1]) == False
assert is_contained_in([1, 2, 3], [4, 5, 6]) == False
```
