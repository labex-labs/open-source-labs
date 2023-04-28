# Date is Weekend

## Introduction
In Python, the `datetime` module provides classes for working with dates and times. One common task is to check whether a given date is a weekend or not. In this challenge, you will write a function that takes a date as input and returns `True` if it is a weekend, and `False` otherwise.

## Problem
Write a function `is_weekend(d)` that takes a date object as input and returns `True` if the given date is a weekend, and `False` otherwise. If no argument is provided, the function should use the current date.

To solve this problem, you can follow these steps:
1. Use the `datetime.datetime.weekday()` method to get the day of the week as an integer.
2. Check if the day of the week is greater than `4`. If it is, return `True`, otherwise return `False`.

## Example
```python
from datetime import date

assert is_weekend(date(2022, 1, 1)) == True
assert is_weekend(date(2022, 1, 3)) == False
assert is_weekend() == False # current date is not a weekend
```

## Summary
In this challenge, you have learned how to write a Python function that checks whether a given date is a weekend or not. You have used the `datetime` module to get the day of the week as an integer, and checked if it is greater than `4` to determine whether the date is a weekend or not.