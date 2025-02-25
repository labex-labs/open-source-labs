# Diviser une liste en morceaux

## Problème

Écrivez une fonction `chunk(lst, size)` qui prend une liste `lst` et un entier positif `size` en arguments et renvoie une liste de listes plus petites, dont chacune a une taille maximale de `size`. Si la longueur de `lst` n'est pas divisible uniformément par `size`, la dernière liste de la liste renvoyée devrait contenir les éléments restants.

## Exemple

```python
chunk([1, 2, 3, 4, 5], 2) # [[1, 2], [3, 4], [5]]
chunk([1, 2, 3, 4, 5], 3) # [[1, 2, 3], [4, 5]]
chunk([1, 2, 3, 4, 5], 1) # [[1], [2], [3], [4], [5]]
```
