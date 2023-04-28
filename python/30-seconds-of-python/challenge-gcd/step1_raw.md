---
title: Greatest common divisor
---

Calculates the greatest common divisor of a list of numbers.

- Use `functools.reduce()` and `math.gcd()` over the given list.

```py
from functools import reduce
from math import gcd as _gcd

def gcd(numbers):
  return reduce(_gcd, numbers)
```

```py
gcd([8, 36, 28]) # 4
```
