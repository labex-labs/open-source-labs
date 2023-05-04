# Check if any value in a list is included in another list

## Introduction

In this challenge, you will write a function to check if any element in a given list is included in another given list.

## Problem

Write a function `includes_any(lst, values)` that takes in two lists as arguments. The function should check if any element in `values` is included in `lst`. If any one value is found, the function should return `True`, otherwise, it should return `False`.

To solve this problem, you can use a `for` loop to iterate through each value in `values`. Then, you can use the `in` operator to check if the value is included in `lst`. If a value is found, return `True`. If no value is found, return `False`.

## Example

```python
includes_any([1, 2, 3, 4], [2, 9]) # True
includes_any([1, 2, 3, 4], [8, 9]) # False
```

## Summary

In this challenge, you learned how to check if any element in a given list is included in another given list. You used a `for` loop to iterate through each value in `values` and the `in` operator to check if the value is included in `lst`. You then returned `True` if any one value was found, and `False` otherwise.
