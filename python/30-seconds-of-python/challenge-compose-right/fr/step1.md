# Composer les fonctions dans l'ordre inverse

## Problème

Écrivez une fonction `compose_right` qui prend une ou plusieurs fonctions en arguments et renvoie une nouvelle fonction qui effectue une composition de fonctions de gauche à droite. La première fonction (la plus à gauche) peut accepter un ou plusieurs arguments ; les fonctions suivantes doivent être unaire.

Votre implémentation devrait utiliser la fonction `reduce` du module `functools` pour effectuer une composition de fonctions de gauche à droite.

```python
from functools import reduce

def compose_right(*fns):
  # votre code ici
```

## Exemple

```python
add = lambda x, y: x + y
square = lambda x: x * x
add_and_square = compose_right(add, square)
assert add_and_square(1, 2) == 9
```

Dans l'exemple ci-dessus, nous définissons deux fonctions `add` et `square`. Nous utilisons ensuite la fonction `compose_right` pour créer une nouvelle fonction `add_and_square` qui additionne d'abord deux nombres puis calcule le carré du résultat. Nous appelons ensuite la fonction `add_and_square` avec les arguments `1` et `2`, ce qui renvoie `9`.
