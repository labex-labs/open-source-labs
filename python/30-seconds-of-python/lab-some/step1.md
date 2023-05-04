# Test if some list elements are truthy

Write a function `some(lst, fn)` that takes a list `lst` and a function `fn` as arguments. The function should return `True` if the function `fn` returns `True` for at least one element in the list `lst`. If no element in the list satisfies the condition, the function should return `False`. If no function is provided, the function should use the identity function (which returns the element itself).

```py
def some(lst, fn = lambda x: x):
  return any(map(fn, lst))
```

```py
some([0, 1, 2, 0], lambda x: x >= 2 ) # True
some([0, 0, 1, 0]) # True
```
