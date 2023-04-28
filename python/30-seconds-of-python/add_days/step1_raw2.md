# Add Days to Date

## Introduction
In Python, you can easily add or subtract days from a given date using the `datetime` module. This can be useful in various scenarios, such as calculating the due date of a task or project, or determining the date after a certain number of days from a given date.

## Problem
Write a function `add_days(n, d)` that takes in two arguments:
- `n`: an integer representing the number of days to add (if positive) or subtract (if negative) from the given date.
- `d`: an optional argument representing the date to which the days should be added or subtracted. If not provided, the current date should be used.

The function should return a `datetime` object representing the new date after adding or subtracting the specified number of days.

## Example
```python
from datetime import date

add_days(5, date(2020, 10, 25)) # returns datetime.date(2020, 10, 30)
add_days(-5, date(2020, 10, 25)) # returns datetime.date(2020, 10, 20)
```

## Summary
In this challenge, you learned how to add or subtract days from a given date using the `datetime` module in Python. You also wrote a function that takes in a number of days and a date, and returns a new date after adding or subtracting the specified number of days.