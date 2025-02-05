# 最小公倍数

编写一个函数 `lcm(numbers)`，它接受一个数字列表作为参数，并返回它们的最小公倍数。你的函数应该使用以下公式来计算两个数字 `x` 和 `y` 的最小公倍数：`lcm(x, y) = x * y / gcd(x, y)`，其中 `gcd(x, y)` 是 `x` 和 `y` 的最大公约数。

要解决这个问题，你可以使用 `functools.reduce()` 函数将 `lcm()` 公式应用于列表中的所有数字。你也可以使用 `math.gcd()` 函数来计算两个数字的最大公约数。

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
