# Median Challenge

## Introduction
In statistics, the median is a measure of central tendency that represents the middle value of a dataset. It is the value separating the higher half from the lower half of a data sample. In this challenge, you will be required to write a Python function that finds the median of a list of numbers.

## Problem
Write a Python function called `find_median` that takes a list of numbers as an argument and returns the median of the list. Your function should perform the following steps:

1. Sort the numbers of the list using `list.sort()`.
2. Find the median, which is either the middle element of the list if the list length is odd or the average of the two middle elements if the list length is even.
3. Return the median.

Your function should not use any built-in Python libraries or functions that directly solve the problem.

## Example
```py
find_median([1, 2, 3]) # 2.0
find_median([1, 2, 3, 4]) # 2.5
```

## Summary
In this challenge, you have learned how to find the median of a list of numbers using Python. You have written a function that sorts the list and finds the median by checking the length of the list and returning the appropriate value.