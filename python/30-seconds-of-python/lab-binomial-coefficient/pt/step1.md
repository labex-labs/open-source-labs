# Coeficiente Binomial

Escreva uma função chamada `binomial_coefficient(n, k)` que recebe dois inteiros `n` e `k` e retorna o coeficiente binomial de `n` e `k`. Sua função deve usar o método `math.comb()` para calcular o coeficiente binomial.

```python
from math import comb

def binomial_coefficient(n, k):
  return comb(n, k)
```

```python
binomial_coefficient(8, 2) # 28
```
