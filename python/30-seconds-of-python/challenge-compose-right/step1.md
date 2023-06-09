# Reverse Compose Functions

## Problem

Write a function `compose_right` that takes one or more functions as arguments and returns a new function that performs left-to-right function composition. The first (leftmost) function can accept one or more arguments; the remaining functions must be unary.

Your implementation should use the `reduce` function from the `functools` module to perform left-to-right function composition.

```python
from functools import reduce

def compose_right(*fns):
  # your code here
```

## Example

```python
add = lambda x, y: x + y
square = lambda x: x * x
add_and_square = compose_right(add, square)
assert add_and_square(1, 2) == 9
```

In the example above, we define two functions `add` and `square`. We then use the `compose_right` function to create a new function `add_and_square` that first adds two numbers and then squares the result. We then call the `add_and_square` function with the arguments `1` and `2`, which returns `9`.
