# N éléments les plus petits

## Problème

Écrivez une fonction appelée `min_n(lst, n = 1)` qui prend une liste `lst` et un entier optionnel `n` (valeur par défaut de `1`). La fonction devrait renvoyer une nouvelle liste contenant les `n` plus petits éléments de la liste d'origine `lst`. Si `n` n'est pas fourni, la fonction devrait renvoyer une liste contenant le plus petit élément de `lst`.

Si `n` est supérieur ou égal à la longueur de `lst`, la fonction devrait renvoyer la liste d'origine triée par ordre croissant.

Votre fonction devrait accomplir cela en suivant ces étapes :

1. Utilisez la fonction intégrée `sorted()` pour trier la liste par ordre croissant.
2. Utilisez la notation de tranche pour obtenir le nombre spécifié d'éléments.
3. Retournez la liste résultante.

## Exemple

```python
min_n([1, 2, 3]) # [1]
min_n([1, 2, 3], 2) # [1, 2]
```
