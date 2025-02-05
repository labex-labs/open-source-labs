# 判断数字是否为质数

编写一个名为 `is_prime(n)` 的Python函数，该函数接受一个整数 `n` 作为输入，如果该数字是质数，则返回 `True`，否则返回 `False`。要解决这个问题，你需要遵循以下规则：

- 如果数字为0、1、负数或2的倍数，则返回 `False`。
- 使用 `all()` 和 `range()` 检查从3到给定数字的平方根的数字。
- 如果没有数字能整除给定数字，则返回 `True`，否则返回 `False`。

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
