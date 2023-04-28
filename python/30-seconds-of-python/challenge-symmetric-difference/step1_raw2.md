# Symmetric Difference

## Introduction
In Python, the symmetric difference between two sets is the set of elements that are in either of the sets, but not in their intersection. In this challenge, you will write a function that takes two lists as input and returns their symmetric difference.

## Problem
Write a function `symmetric_difference(a, b)` that takes two lists as arguments and returns their symmetric difference as a list. The function should not filter out duplicate values.

To solve this problem, you can follow these steps:
1. Create a set from each list.
2. Use a list comprehension on each of them to only keep values not contained in the previously created set of the other.
3. Concatenate the two lists obtained in step 2.

## Example
```py
symmetric_difference([1, 2, 3], [1, 2, 4]) # [3, 4]
```

## Summary
In this challenge, you have learned how to find the symmetric difference between two lists in Python. You have also learned how to use sets and list comprehensions to solve this problem.