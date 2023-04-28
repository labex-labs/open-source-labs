# Most Frequent Element

## Introduction

In this challenge, you are required to write a Python function that takes a list of integers as input and returns the most frequent element in the list.

## Problem

Write a Python function called `most_frequent(lst)` that takes a list of integers as input and returns the most frequent element in the list. If there are multiple elements that appear the same number of times and have the highest frequency, return the one that appears first in the list.

To solve this problem, you can follow these steps:

1. Use `set()` to get the unique values in `lst`.
2. Use `max()` to find the element that has the most appearances.

Your function should have the following signature:

```python
def most_frequent(lst: List[int]) -> int:
```

## Example

```python
assert most_frequent([1, 2, 1, 2, 3, 2, 1, 4, 2]) == 2
assert most_frequent([1, 2, 3, 4, 5]) == 1
assert most_frequent([1, 1, 1, 1, 1]) == 1
```

## Summary

In this challenge, you have learned how to find the most frequent element in a list of integers using Python. You have also learned how to use the `set()` and `max()` functions to solve this problem.
