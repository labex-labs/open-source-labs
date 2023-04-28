# Apply Function When True

## Problem

Write a function called `when` that takes two arguments: a predicate function `predicate` and a function to apply `when_true`. The `when` function should return a new function that takes a single argument `x`. The new function should check if the value of `predicate(x)` is `True`. If it is, the new function should call `when_true(x)` and return the result. Otherwise, the new function should return `x`.

## Example

```py
def double(x):
    return x * 2

def is_even(x):
    return x % 2 == 0

double_even_numbers = when(is_even, double)
double_even_numbers(2) # 4
double_even_numbers(1) # 1
```
