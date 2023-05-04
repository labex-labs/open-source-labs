# List Difference

## Introduction

In Python, we can calculate the difference between two lists or any iterable objects. The difference between two lists is the elements that are present in the first list but not in the second list. In this challenge, you will be required to write a Python function that takes two lists as arguments and returns the difference between them.

## Problem

Write a Python function called `list_difference(a, b)` that takes two lists as arguments and returns the difference between them. The function should not filter out duplicate values. To solve this problem, you can follow these steps:

1. Create a set from the second list `b`.
2. Use a list comprehension on the first list `a` to only keep values not contained in the previously created set `_b`.
3. Return the resulting list.

## Example

```py
list_difference([1, 2, 3], [1, 2, 4]) # [3]
```

## Summary

In this challenge, you have learned how to calculate the difference between two lists in Python. You have also learned how to use sets and list comprehension to solve this problem. Now, you can use this knowledge to write more efficient and concise Python code.
