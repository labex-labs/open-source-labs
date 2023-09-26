# Compose Functions

Write a function called `compose(*fns)` that accepts one or more functions as arguments and returns a new function that is the result of composing the input functions from right to left. The last (rightmost) function can accept one or more arguments; the remaining functions must be unary.

```python
from functools import reduce

def compose(*fns):
  return reduce(lambda f, g: lambda *args: f(g(*args)), fns)
```

```python
add5 = lambda x: x + 5
multiply = lambda x, y: x * y
multiply_and_add_5 = compose(add5, multiply)
multiply_and_add_5(5, 2) # 15
```
