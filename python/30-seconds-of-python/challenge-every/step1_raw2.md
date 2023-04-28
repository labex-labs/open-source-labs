# Test if every list element is truthy

## Introduction
In Python, we can use the `all()` function to check if all elements in a list are truthy. However, sometimes we may want to check if a specific condition is true for every element in the list. In this challenge, you will need to create a function that checks if a provided function returns `True` for every element in the list.

## Problem
Write a function called `every(lst, fn = lambda x: x)` that takes a list `lst` and a function `fn` as arguments. The function should return `True` if `fn` returns `True` for every element in the list, and `False` otherwise. If no function is provided, the function should use the identity function (`lambda x: x`) by default.

To solve this problem, you will need to use the `all()` function in combination with `map()` and the provided function `fn` to check if `fn` returns `True` for all elements in the list.

## Example
```py
every([4, 2, 3], lambda x: x > 1) # True
every([1, 2, 3]) # True
every([0, 1, 2]) # False
```

## Summary
In this challenge, you have learned how to create a function that checks if a provided function returns `True` for every element in a list. You have used the `all()` function in combination with `map()` and the provided function to solve the problem.