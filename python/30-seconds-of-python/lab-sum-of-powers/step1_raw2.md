# Sum of powers Challenge

## Introduction

In this challenge, you are required to write a Python function that calculates the sum of the powers of all the numbers from `start` to `end` (both inclusive).

## Problem

Write a Python function called `sum_of_powers` that takes in three parameters:

- `end` - an integer representing the end of the range (inclusive)
- `power` - an integer representing the power to which each number in the range should be raised (default value is 2)
- `start` - an integer representing the start of the range (default value is 1)

The function should return the sum of the powers of all the numbers from `start` to `end` (both inclusive).

To solve this problem, you can follow these steps:

1. Use `range()` in combination with a list comprehension to create a list of elements in the desired range raised to the given `power`.
2. Use `sum()` to add the values together.

## Example

```py
sum_of_powers(10) # returns 385
sum_of_powers(10, 3) # returns 3025
sum_of_powers(10, 3, 5) # returns 2925
```

## Summary

In this challenge, you have learned how to write a Python function that calculates the sum of the powers of all the numbers from `start` to `end` (both inclusive). This challenge will help you to improve your Python programming skills.
