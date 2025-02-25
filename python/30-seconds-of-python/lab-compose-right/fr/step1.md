# Reverse Compose Functions

Écrivez une fonction `compose_right` qui prend une ou plusieurs fonctions en arguments et renvoie une nouvelle fonction qui effectue une composition de fonctions de gauche à droite. La première (la plus à gauche) fonction peut accepter un ou plusieurs arguments ; les fonctions suivantes doivent être unaires.

Votre implémentation devrait utiliser la fonction `reduce` du module `functools` pour effectuer une composition de fonctions de gauche à droite.

```python
from functools import reduce

def compose_right(*fns):
  # votre code ici
```

```python
from functools import reduce

def compose_right(*fns):
  return reduce(lambda f, g: lambda *args: g(f(*args)), fns)
```

```python
add = lambda x, y: x + y
square = lambda x: x * x
add_and_square = compose_right(add, square)
add_and_square(1, 2) # 9
```
