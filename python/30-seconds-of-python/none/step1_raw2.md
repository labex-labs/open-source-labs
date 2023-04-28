# Test if every list element is falsy

## Introduction
In Python, we can use the `all()` function to check if all elements in a list are truthy. But what if we want to check if every element in a list is falsy? In this challenge, you will need to create a function that checks if every element in a list is falsy.

## Problem
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

## Example
```python
assert none([0, 1, 2, 0], lambda x: x >= 2 ) == False
assert none([0, 0, 0]) == True
```

## Summary
In this challenge, you learned how to create a Python function that checks if every element in a list is falsy. You also learned how to use an optional function to determine the truthiness of each element in the list.