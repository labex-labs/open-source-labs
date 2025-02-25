# Composer des fonctions

Écrivez une fonction appelée `compose(*fns)` qui accepte une ou plusieurs fonctions en tant qu'arguments et renvoie une nouvelle fonction qui est le résultat de la composition des fonctions d'entrée de droite à gauche. La dernière (la plus à droite) fonction peut accepter un ou plusieurs arguments ; les fonctions restantes doivent être unaires.

```python
from functools import reduce

def compose(*fns):
  return reduce(lambda f, g: lambda *args: f(g(*args)), fns)
```

```python
add5 = lambda x: x + 5
multiply = lambda x, y: x * y
multiply_and_add_5 = compose(add5, multiply)
multiply_and_add_5(5, 2) # 15
```
