# Binomial Coefficient

Write a function called `binomial_coefficient(n, k)` that takes in two integers `n` and `k` and returns the binomial coefficient of `n` and `k`. Your function should use the `math.comb()` method to calculate the binomial coefficient.

```python
from math import comb

def binomial_coefficient(n, k):
  return comb(n, k)
```

```python
binomial_coefficient(8, 2) # 28
```
