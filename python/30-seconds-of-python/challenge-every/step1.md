# Test if every list element is truthy

## Problem

Write a function called `every(lst, fn = lambda x: x)` that takes a list `lst` and a function `fn` as arguments. The function should return `True` if `fn` returns `True` for every element in the list, and `False` otherwise. If no function is provided, the function should use the identity function (`lambda x: x`) by default.

To solve this problem, you will need to use the `all()` function in combination with `map()` and the provided function `fn` to check if `fn` returns `True` for all elements in the list.

## Example

```py
every([4, 2, 3], lambda x: x > 1) # True
every([1, 2, 3]) # True
every([0, 1, 2]) # False
```
