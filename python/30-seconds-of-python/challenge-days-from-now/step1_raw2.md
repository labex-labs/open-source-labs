# Days from now

## Introduction

In Python, you can easily calculate the date of `n` days from today using the `datetime` module. In this challenge, you will be asked to write a function that takes an integer `n` as input and returns the date of `n` days from today.

## Problem

Write a function `days_from_now(n)` that takes an integer `n` as input and returns the date of `n` days from today.

To solve this problem, you can follow these steps:

1. Import the `datetime` module.
2. Use the `date.today()` method to get the current date.
3. Use the `timedelta` method to add `n` days to the current date.
4. Return the new date.

## Example

```python
>>> days_from_now(5)
datetime.date(2022, 12, 28)
>>> days_from_now(10)
datetime.date(2022, 1, 2)
```

## Summary

In this challenge, you learned how to calculate the date of `n` days from today using the `datetime` module in Python. You can use this function to perform various date calculations in your Python programs.
