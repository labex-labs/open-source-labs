# Date Range Challenge

## Introduction

In Python, the `datetime` module provides classes for working with dates and times. One common task is to create a list of dates between two given dates. In this challenge, you will create a function that takes two dates as input and returns a list of all the dates between them.

## Problem

Write a Python function called `daterange(start, end)` that takes two `datetime.date` objects as arguments and returns a list of all the dates between them. The list should include the start date but not the end date.

To solve this problem, you can follow these steps:

1. Use `datetime.timedelta.days` to get the number of days between `start` and `end`.
2. Use `int()` to convert the result to an integer and `range()` to iterate over each day.
3. Use a list comprehension and `datetime.timedelta` to create a list of `datetime.date` objects.

## Example

```py
from datetime import date

daterange(date(2020, 10, 1), date(2020, 10, 5))
# [date(2020, 10, 1), date(2020, 10, 2), date(2020, 10, 3), date(2020, 10, 4)]
```

## Summary

In this challenge, you have learned how to create a list of dates between two given dates using the `datetime` module in Python. You can use this function to solve a variety of problems, such as calculating the number of days between two dates or generating a list of dates for a given month or year.
