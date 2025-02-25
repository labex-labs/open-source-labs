# Le nombre est premier

Écrivez une fonction Python appelée `is_prime(n)` qui prend un entier `n` en entrée et renvoie `True` si le nombre est premier, et `False` sinon. Pour résoudre ce problème, vous devez suivre ces règles :

- Retournez `False` si le nombre est `0`, `1`, un nombre négatif ou un multiple de `2`.
- Utilisez `all()` et `range()` pour vérifier les nombres de `3` à la racine carrée du nombre donné.
- Retournez `True` si aucun nombre ne divise le nombre donné, `False` sinon.

```python
from math import sqrt

def is_prime(n):
  if n <= 1 or (n % 2 == 0 and n > 2):
    return False
  return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))
```

```python
is_prime(11) # True
```
