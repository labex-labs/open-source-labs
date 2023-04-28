# Test if some list elements are truthy

## Introduction
In Python, we can use the `any()` function to check if at least one element in a list is `True`. In this challenge, you will need to create a function that takes a list and a function as arguments, and returns `True` if the function returns `True` for at least one element in the list.

## Problem
Write a function `some(lst, fn)` that takes a list `lst` and a function `fn` as arguments. The function should return `True` if the function `fn` returns `True` for at least one element in the list `lst`. If no element in the list satisfies the condition, the function should return `False`. If no function is provided, the function should use the identity function (which returns the element itself).

## Example
```python
some([0, 1, 2, 0], lambda x: x >= 2 ) # True
some([0, 0, 1, 0]) # True
some(['', 'hello', 'world'], bool) # True
some(['', '', ''], bool) # False
```

## Summary
In this challenge, you learned how to use the `any()` function in combination with `map()` to check if a function returns `True` for at least one element in a list. You also created a function that takes a list and a function as arguments, and returns `True` if the function returns `True` for at least one element in the list.