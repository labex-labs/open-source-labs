# Drop List Elements from the Left

## Introduction

In Python, we can use slice notation to remove elements from a list. In this challenge, you will need to write a function that removes a specified number of elements from the left of a list.

## Problem

Write a function `drop(a, n=1)` that takes a list `a` and an optional integer `n` as arguments and returns a new list with `n` elements removed from the left of the original list. If `n` is not provided, the function should remove only the first element of the list.

## Example

```py
drop([1, 2, 3]) # [2, 3]
drop([1, 2, 3], 2) # [3]
drop([1, 2, 3], 42) # []
```

## Summary

In this challenge, you learned how to use slice notation to remove elements from a list in Python. You also wrote a function that removes a specified number of elements from the left of a list.
