# Digitize Number

Écrivez une fonction `digitize(n)` qui prend un entier non négatif `n` en entrée et renvoie une liste de ses chiffres. La fonction devrait accomplir cela en effectuant les étapes suivantes :

1. Convertir le nombre d'entrée `n` en une chaîne de caractères.
2. Utiliser la fonction `map()` combinée avec la fonction `int` pour convertir chaque caractère de la chaîne en un entier.
3. Retourner la liste d'entiers résultante.

Par exemple, si le nombre d'entrée est `123`, la fonction devrait renvoyer la liste `[1, 2, 3]`.

```python
def digitize(n):
  return list(map(int, str(n)))
```

```python
digitize(123) # [1, 2, 3]
```
