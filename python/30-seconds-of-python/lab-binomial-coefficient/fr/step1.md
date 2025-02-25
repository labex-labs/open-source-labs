# Coefficient binomial

Écrivez une fonction appelée `binomial_coefficient(n, k)` qui prend deux entiers `n` et `k` et renvoie le coefficient binomial de `n` et `k`. Votre fonction devrait utiliser la méthode `math.comb()` pour calculer le coefficient binomial.

```python
from math import comb

def binomial_coefficient(n, k):
  return comb(n, k)
```

```python
binomial_coefficient(8, 2) # 28
```
