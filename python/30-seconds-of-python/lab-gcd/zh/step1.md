# 最大公因数

编写一个名为 `gcd(numbers)` 的函数，它接受一个整数列表作为参数，并返回这些整数的最大公因数。你的函数应该对给定列表使用 `functools.reduce()` 和 `math.gcd()`。

```python
from functools import reduce
from math import gcd as _gcd

def gcd(numbers):
  return reduce(_gcd, numbers)
```

```python
gcd([8, 36, 28]) # 4
```
