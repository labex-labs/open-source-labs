# Find Parity Outliers

## Introduction

In this challenge, you are tasked with finding the parity outliers in a given list. Parity outliers are elements in a list that have a different parity (odd or even) than the majority of the elements in the list.

## Problem

Write a function `find_parity_outliers(nums)` that takes a list of integers `nums` as an argument and returns a list of all the parity outliers in `nums`.

To solve this problem, you can follow these steps:

1. Use `collections.Counter` with a list comprehension to count even and odd values in the list.
2. Use `collections.Counter.most_common()` to get the most common parity.
3. Use a list comprehension to find all elements that do not match the most common parity.

## Example

```py
find_parity_outliers([1, 2, 3, 4, 6]) # [1, 3]
```

In the example above, the majority of the elements in the list are even, so the parity outliers are the odd elements 1 and 3.

## Summary

In this challenge, you learned how to find the parity outliers in a list of integers. You used the `collections.Counter` module to count even and odd values in the list, and then found the most common parity. Finally, you used a list comprehension to find all elements that do not match the most common parity.
