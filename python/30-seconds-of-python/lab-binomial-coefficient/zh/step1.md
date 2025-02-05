# 二项式系数

编写一个名为 `binomial_coefficient(n, k)` 的函数，它接受两个整数 `n` 和 `k`，并返回 `n` 和 `k` 的二项式系数。你的函数应该使用 `math.comb()` 方法来计算二项式系数。

```python
from math import comb

def binomial_coefficient(n, k):
  return comb(n, k)
```

```python
binomial_coefficient(8, 2) # 28
```
