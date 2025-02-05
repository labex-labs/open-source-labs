# Reverse Compose Functions

Write a function `compose_right` that takes one or more functions as arguments and returns a new function that performs left-to-right function composition. The first (leftmost) function can accept one or more arguments; the remaining functions must be unary.

Your implementation should use the `reduce` function from the `functools` module to perform left-to-right function composition.

```python
from functools import reduce

def compose_right(*fns):
  # your code here
```

```python
from functools import reduce

def compose_right(*fns):
  return reduce(lambda f, g: lambda *args: g(f(*args)), fns)
```

```python
add = lambda x, y: x + y
square = lambda x: x * x
add_and_square = compose_right(add, square)
add_and_square(1, 2) # 9
```
