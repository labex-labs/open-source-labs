# Curry Function

Write a function `curry(fn, *args)` that curries a given function `fn`. The function should return a new function that behaves like `fn` with the given arguments, `args`, partially applied.

```python
from functools import partial

def curry(fn, *args):
  return partial(fn, *args)
```

```python
add = lambda x, y: x + y
add10 = curry(add, 10)
add10(20) # 30
```
