# Greatest Common Divisor

Write a function called `gcd(numbers)` that takes a list of integers as an argument and returns their greatest common divisor. Your function should use `functools.reduce()` and `math.gcd()` over the given list.

```python
from functools import reduce
from math import gcd as _gcd

def gcd(numbers):
  return reduce(_gcd, numbers)
```

```python
gcd([8, 36, 28]) # 4
```
