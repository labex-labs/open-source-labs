# Title

N Max Elements Challenge

## Introduction

In Python, there are many ways to manipulate lists. One common task is to find the `n` maximum elements from a list. In this challenge, you will be asked to write a function that returns the `n` maximum elements from a list.

## Problem

Write a function `max_n(lst, n = 1)` that takes a list `lst` and an optional integer `n` as arguments and returns a list of the `n` maximum elements from the provided list. If `n` is not provided, the function should return a list containing the maximum element of the list. If `n` is greater than or equal to the length of the list, the function should return the original list sorted in descending order.

Your task is to implement the `max_n()` function.

## Example

```py
max_n([1, 2, 3]) # [3]
max_n([1, 2, 3], 2) # [3, 2]
max_n([1, 2, 3, 4, 5], 3) # [5, 4, 3]
max_n([1, 2, 3, 4, 5], 6) # [5, 4, 3, 2, 1]
```

## Summary

In this challenge, you have learned how to find the `n` maximum elements from a list in Python. You have implemented a function that takes a list and an optional integer as arguments and returns a list of the `n` maximum elements from the provided list.