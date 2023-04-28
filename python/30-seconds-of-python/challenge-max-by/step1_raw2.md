# Find Maximum List Value Based on Function

## Introduction

In Python, we can use the `max()` function to find the maximum value in a list. However, what if we want to find the maximum value after mapping each element to a value using a provided function? In this challenge, you will need to write a function that takes a list and a function as arguments, maps each element to a value using the provided function, and returns the maximum value.

## Problem

Write a function `max_by(lst, fn)` that takes a list `lst` and a function `fn` as arguments. The function should map each element in `lst` to a value using the provided function `fn`, and then return the maximum value.

### Example

```python
max_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 8
```

### Constraints

* The list `lst` will contain at least one element.
* The function `fn` will take one argument and return a value.

## Summary

In this challenge, you have learned how to find the maximum value in a list after mapping each element to a value using a provided function. You have written a function `max_by(lst, fn)` that takes a list and a function as arguments, maps each element to a value using the provided function, and returns the maximum value.