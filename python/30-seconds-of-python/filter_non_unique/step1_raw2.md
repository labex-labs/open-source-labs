# Filter Non-Unique List Values

## Introduction
In Python, a list is a collection of items that can be of different data types. Sometimes, we need to filter out the non-unique values from a list. In this challenge, you will create a function that takes a list as an argument and returns a new list with only the unique values.

## Problem
Write a Python function called `filter_non_unique(lst)` that takes a list as an argument and returns a new list with only the unique values. To solve this problem, you can follow these steps:
1. Use the `collections.Counter` method to get the count of each value in the list.
2. Use a list comprehension to create a list containing only the unique values.

## Example
```python
filter_non_unique([1, 2, 2, 3, 4, 4, 5]) # [1, 3, 5]
filter_non_unique(['apple', 'banana', 'apple', 'orange', 'pear', 'banana']) # ['orange', 'pear']
```

## Summary
In this challenge, you have learned how to filter out non-unique values from a list using the `collections.Counter` method and a list comprehension. This is a useful technique to have in your Python programming toolbox.