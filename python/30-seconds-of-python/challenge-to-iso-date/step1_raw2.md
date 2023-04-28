# Date to ISO format

## Introduction
In Python, dates can be represented in different formats. One of the most common formats is the ISO-8601 format, which represents dates and times in a standardized way. In this challenge, you will write a function that converts a date to its ISO-8601 representation.

## Problem
Write a function `to_iso_date(d)` that takes a `datetime.datetime` object as its argument and returns a string representing the date in ISO-8601 format. The function should use the `datetime.datetime.isoformat()` method to convert the date to its ISO-8601 representation.

## Example
```py
from datetime import datetime

to_iso_date(datetime(2020, 10, 25)) # "2020-10-25T00:00:00"
```

## Summary
In this challenge, you wrote a function that converts a date to its ISO-8601 representation. You learned how to use the `datetime.datetime.isoformat()` method to convert a `datetime.datetime` object to an ISO-8601 date.