# Date Difference Challenge

## Introduction

In Python, you can calculate the difference between two dates using the `datetime` module. This challenge will test your ability to calculate the month difference between two dates.

## Problem

Write a function called `months_diff(start, end)` that takes in two date objects and returns the month difference between them. The function should:

1. Subtract `start` from `end` and use `datetime.timedelta.days` to get the day difference.
2. Divide by `30` and use `math.ceil()` to get the difference in months (rounded up).

## Example

```py
from datetime import date

months_diff(date(2020, 10, 28), date(2020, 11, 25)) # 1
```

## Summary

In this challenge, you learned how to calculate the month difference between two dates in Python. Remember to use the `datetime` module to subtract the dates and `math.ceil()` to round up the result. Good luck!
