# Days Ago Challenge

## Introduction
In Python, the `datetime` module provides classes for working with dates and times. One of the classes in this module is `date`, which represents a date (year, month, day) and provides various methods to work with dates. Another class is `timedelta`, which represents a duration or difference between two dates or times.

## Problem
Your task is to write a function called `days_ago(n)` that takes an integer `n` as an argument and returns the date of `n` days ago from today. 

To solve this problem, you need to use the `date` class from the `datetime` module to get the current date and the `timedelta` class to subtract `n` days from the current date.

## Example
```py
days_ago(5) # date(2022, 11, 23)
```

## Summary
In this challenge, you learned how to use the `date` and `timedelta` classes from the `datetime` module to calculate the date of `n` days ago from today. This is a useful skill when working with dates and times in Python.