# Number in Range

## Introduction

In Python, we can check if a given number falls within a specified range using arithmetic comparison. This is a common task in programming and can be useful in many different applications.

## Problem

Write a function `in_range(n, start, end = 0)` that takes in three parameters:

- `n`: a number to check if it falls within the range
- `start`: the start of the range
- `end`: the end of the range (optional, default value is 0)

The function should return `True` if the given number `n` falls within the specified range, and `False` otherwise. If the `end` parameter is not specified, the range is considered to be from `0` to `start`.

## Example

```py
in_range(3, 2, 5) # True
in_range(3, 4) # True
in_range(2, 3, 5) # False
in_range(3, 2) # False
```

## Summary

In this challenge, you learned how to check if a given number falls within a specified range using arithmetic comparison in Python. This is a useful skill that can be applied in many different programming applications.
