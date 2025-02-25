# Plus petit commun multiple

Écrivez une fonction `lcm(numbers)` qui prend une liste de nombres en argument et renvoie leur plus petit commun multiple. Votre fonction devrait utiliser la formule suivante pour calculer le PCM de deux nombres `x` et `y` : `lcm(x, y) = x * y / pgcd(x, y)`, où `pgcd(x, y)` est le plus grand diviseur commun de `x` et `y`.

Pour résoudre ce problème, vous pouvez utiliser la fonction `functools.reduce()` pour appliquer la formule `lcm()` à tous les nombres de la liste. Vous pouvez également utiliser la fonction `math.gcd()` pour calculer le plus grand diviseur commun de deux nombres.

```python
from functools import reduce
from math import gcd

def lcm(numbers):
  return reduce((lambda x, y: int(x * y / gcd(x, y))), numbers)
```

```python
lcm([12, 7]) # 84
lcm([1, 3, 4, 5]) # 60
```
