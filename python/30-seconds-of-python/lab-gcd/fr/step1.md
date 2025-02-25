# Plus grand commun diviseur

Écrivez une fonction appelée `gcd(numbers)` qui prend une liste d'entiers en argument et renvoie leur plus grand commun diviseur. Votre fonction devrait utiliser `functools.reduce()` et `math.gcd()` sur la liste donnée.

```python
from functools import reduce
from math import gcd as _gcd

def gcd(numbers):
  return reduce(_gcd, numbers)
```

```python
gcd([8, 36, 28]) # 4
```
