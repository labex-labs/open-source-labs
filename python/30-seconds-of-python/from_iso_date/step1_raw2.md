# Convert ISO Date

## Introduction
In Python, dates can be represented in various formats. One such format is the ISO-8601 format, which is a standard format for representing dates and times. In this challenge, you will be tasked with converting a date from its ISO-8601 representation to a `datetime.datetime` object.

## Problem
Write a function `from_iso_date(d)` that takes a string `d` representing a date in ISO-8601 format and returns a `datetime.datetime` object representing the same date and time.

## Example
```py
from_iso_date('2020-10-28T12:30:59.000000') # returns datetime.datetime(2020, 10, 28, 12, 30, 59)
```

## Summary
In this challenge, you learned how to convert a date from its ISO-8601 representation to a `datetime.datetime` object in Python. This can be useful when working with dates and times in various applications.