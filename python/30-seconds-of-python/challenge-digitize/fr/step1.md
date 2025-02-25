# Numériser un nombre

## Problème

Écrivez une fonction `digitize(n)` qui prend un entier non négatif `n` en entrée et renvoie une liste de ses chiffres. La fonction devrait accomplir cela en effectuant les étapes suivantes :

1. Convertissez le nombre d'entrée `n` en chaîne de caractères.
2. Utilisez la fonction `map()` combinée avec la fonction `int` pour convertir chaque caractère de la chaîne en un entier.
3. Retournez la liste résultante d'entiers.

Par exemple, si le nombre d'entrée est `123`, la fonction devrait renvoyer la liste `[1, 2, 3]`.

## Exemple

```python
assert digitize(123) == [1, 2, 3]
assert digitize(4567) == [4, 5, 6, 7]
assert digitize(0) == [0]
```
