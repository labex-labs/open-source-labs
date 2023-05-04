# Number is Prime

Write a Python function called `is_prime(n)` that takes an integer `n` as input and returns `True` if the number is prime, and `False` otherwise. To solve this problem, you need to follow these rules:

- Return `False` if the number is `0`, `1`, a negative number or a multiple of `2`.
- Use `all()` and `range()` to check numbers from `3` to the square root of the given number.
- Return `True` if none divides the given number, `False` otherwise.

```py
from math import sqrt

def is_prime(n):
  if n <= 1 or (n % 2 == 0 and n > 2):
    return False
  return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))
```

```py
is_prime(11) # True
```
