# Initialize List with Range

## Introduction

In Python, you can create a list of numbers using the `range()` function. However, sometimes you may want to create a list of numbers that are not sequential or that start at a different number than 0. In such cases, you can use the `initialize_list_with_range()` function.

## Problem

Write a function `initialize_list_with_range(end, start=0, step=1)` that initializes a list containing the numbers in the specified range where `start` and `end` are inclusive with their common difference `step`.

The function should return a list of the appropriate length, filled with the desired values in the given range.

### Input

- `end` (integer) - The end of the range (inclusive).
- `start` (integer, optional) - The start of the range (inclusive). Default is 0.
- `step` (integer, optional) - The common difference between each number in the range. Default is 1.

### Output

- A list containing the numbers in the specified range.

### Example

```python
initialize_list_with_range(5) # [0, 1, 2, 3, 4, 5]
initialize_list_with_range(7, 3) # [3, 4, 5, 6, 7]
initialize_list_with_range(9, 0, 2) # [0, 2, 4, 6, 8]
```

## Summary

In this challenge, you learned how to create a list of numbers using the `initialize_list_with_range()` function. This function allows you to create a list of numbers that are not sequential or that start at a different number than 0.
