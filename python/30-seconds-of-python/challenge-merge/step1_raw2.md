# Merge Lists

## Introduction

In Python, we can merge two or more lists into a single list using various methods. One such method is to combine elements from each of the input lists based on their positions. In this challenge, you will be tasked with writing a function that merges multiple lists into a list of lists.

## Problem

Write a function called `merge(*args, fill_value=None)` that takes in two or more lists as arguments and returns a list of lists. The function should combine elements from each of the input lists based on their positions. If a list is shorter than the longest list, the function should use `fill_value` for the remaining items. If `fill_value` is not provided, it should default to `None`.

Your task is to implement the `merge()` function.

## Example

```python
merge(['a', 'b'], [1, 2], [True, False]) # [['a', 1, True], ['b', 2, False]]
merge(['a'], [1, 2], [True, False]) # [['a', 1, True], [None, 2, False]]
merge(['a'], [1, 2], [True, False], fill_value = '_')
# [['a', 1, True], ['_', 2, False]]
```

## Summary

In this challenge, you learned how to merge two or more lists into a list of lists in Python. You also learned how to use the `max()` function, list comprehension, and the `range()` function to solve the problem. Remember to use the `fill_value` parameter to fill in the missing values in the shorter lists.
