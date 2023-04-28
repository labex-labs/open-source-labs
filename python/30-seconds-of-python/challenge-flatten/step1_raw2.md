# Flatten a List

## Introduction
In Python, a list can contain other lists as elements. This is known as a nested list. Sometimes, we may need to flatten a nested list into a single list. In this challenge, you will be asked to write a function that flattens a list of lists once.

## Problem
Write a Python function called `flatten(lst)` that takes a list of lists as an argument and returns a flattened list. The function should only flatten the list once, meaning that any nested lists within the original list should be flattened, but any nested lists within those nested lists should remain intact.

To solve this problem, you can use a list comprehension to extract each value from sub-lists in order.

## Example
```py
flatten([[1, 2, 3, 4], [5, 6, 7, 8]]) # [1, 2, 3, 4, 5, 6, 7, 8]
```

## Summary
In this challenge, you learned how to write a Python function to flatten a list of lists once. You used a list comprehension to extract each value from sub-lists in order. This is a useful skill to have when working with nested lists in Python.