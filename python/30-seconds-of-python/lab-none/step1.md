# Test if every list element is falsy

Write a Python function called `none(lst, fn = lambda x: x)` that takes a list `lst` and an optional function `fn` as arguments. The function should return `True` if every element in the list is falsy, and `False` otherwise. If the optional function `fn` is provided, it should be used to determine the truthiness of each element in the list.

To determine if an element is falsy, you can use the same rules as Python's `bool()` function. In general, the following values are considered falsy:

- `False`
- `None`
- `0` (integer)
- `0.0` (float)
- `''` (empty string)
- `[]` (empty list)
- `{}` (empty dictionary)
- `()` (empty tuple)
- `set()` (empty set)

If the optional function `fn` is provided, it should take one argument and return a boolean value. The function will be called for each element in the list, and the return value will be used to determine the truthiness of the element.

```py
def none(lst, fn = lambda x: x):
  return all(not fn(x) for x in lst)
```

```py
none([0, 1, 2, 0], lambda x: x >= 2 ) # False
none([0, 0, 0]) # True
```
