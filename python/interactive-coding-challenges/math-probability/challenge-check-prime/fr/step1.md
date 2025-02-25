# Vérifier si un nombre est premier

## Problème

Écrire une fonction Python qui prend un entier en entrée et renvoie `True` si le nombre est premier, et `False` sinon. Si l'entrée n'est pas un entier ou est inférieure à 2, la fonction devrait lever une exception.

Un nombre est considéré premier s'il est divisible uniquement par 1 et lui-même. Par exemple, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 et 97 sont les 25 premiers nombres premiers.

## Exigences

Le programme devrait répondre aux exigences suivantes :

- La fonction devrait prendre un entier en entrée.
- Si l'entrée n'est pas un entier ou est inférieure à 2, la fonction devrait lever une exception.
- La fonction devrait renvoyer `True` si l'entrée est un nombre premier, et `False` sinon.
- Le programme ne devrait pas considérer 1 comme un nombre premier.

## Utilisation exemple

- `check_prime(None)` -> `Exception`
- `check_prime('hello')` -> `Exception`
- `check_prime(1)` -> `False`
- `check_prime(7)` -> `True`
