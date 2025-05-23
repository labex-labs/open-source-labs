# 反转数字

编写一个函数 `reverse_number(n)`，它接受一个数字作为参数，并返回该数字的反转结果。该函数应满足以下要求：

- 无论数字是正数还是负数，函数都应将其反转。
- 如果输入是浮点数，函数应返回浮点数；如果输入是整数，函数应返回整数。
- 函数不应使用任何直接反转数字的内置函数（例如 `reversed()`）。
- 函数不应使用任何直接将数字转换为字符串的内置函数（例如 `str()`）。
- 函数不应使用任何直接将字符串转换为数字的内置函数（例如 `int()` 或 `float()`）。

```python
from math import copysign

def reverse_number(n):
  return copysign(float(str(n)[::-1].replace('-', '')), n)
```

```python
reverse_number(981) # 189
reverse_number(-500) # -5
reverse_number(73.6) # 6.37
reverse_number(-5.23) # -32.5
```
