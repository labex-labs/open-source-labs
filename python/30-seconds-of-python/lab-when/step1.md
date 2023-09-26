# Apply Function When True

Write a function called `when` that takes two arguments: a predicate function `predicate` and a function to apply `when_true`. The `when` function should return a new function that takes a single argument `x`. The new function should check if the value of `predicate(x)` is `True`. If it is, the new function should call `when_true(x)` and return the result. Otherwise, the new function should return `x`.

```python
def when(predicate, when_true):
  return lambda x: when_true(x) if predicate(x) else x
```

```python
double_even_numbers = when(lambda x: x % 2 == 0, lambda x : x * 2)
double_even_numbers(2) # 4
double_even_numbers(1) # 1
```
