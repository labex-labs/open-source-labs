# Coeficiente binomial

Escribe una función llamada `binomial_coefficient(n, k)` que tome dos enteros `n` y `k` y devuelva el coeficiente binomial de `n` y `k`. Tu función debe utilizar el método `math.comb()` para calcular el coeficiente binomial.

```python
from math import comb

def binomial_coefficient(n, k):
  return comb(n, k)
```

```python
binomial_coefficient(8, 2) # 28
```
