# Двоичный коэффициент

Напишите функцию под названием `binomial_coefficient(n, k)`, которая принимает два целых числа `n` и `k` и возвращает двоичный коэффициент `n` и `k`. Ваша функция должна использовать метод `math.comb()` для вычисления двоичного коэффициента.

```python
from math import comb

def binomial_coefficient(n, k):
  return comb(n, k)
```

```python
binomial_coefficient(8, 2) # 28
```
