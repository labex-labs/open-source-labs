# Check if List Elements are Identical

## Introduction

In Python, you can easily check if all elements in a list are identical using a simple function. In this challenge, you will be tasked with creating a function that checks if all elements in a list are identical.

## Problem

Write a function `all_equal(lst)` that takes a list as an argument and returns `True` if all elements in the list are identical, and `False` otherwise.

To solve this problem, you can use the following steps:

1. Use `set()` to eliminate duplicate elements in the list.
2. Use `len()` to check if the length of the set is `1`.
3. If the length of the set is `1`, return `True`. Otherwise, return `False`.

## Example

```python
all_equal([1, 2, 3, 4, 5, 6]) # False
all_equal([1, 1, 1, 1]) # True
```

## Summary

In this challenge, you learned how to check if all elements in a list are identical using a simple function. You can use this function to quickly determine if a list contains only identical elements.
