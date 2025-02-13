# Curry Function

## Problem

Write a function `curry(fn, *args)` that curries a given function `fn`. The function should return a new function that behaves like `fn` with the given arguments, `args`, partially applied.

## Example

```python
add = lambda x, y: x + y
add10 = curry(add, 10)
add10(20) # 30
```
