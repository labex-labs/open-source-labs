## Title

Python Challenge: Value Frequencies

## Introduction

In this challenge, you will create a Python function that takes a list as an argument and returns a dictionary with the unique values of the list as keys and their frequencies as the values. This is a common task in data analysis and can be useful in many different applications.

## Problem

Write a Python function called `value_frequencies(lst)` that takes a list as an argument and returns a dictionary with the unique values of the list as keys and their frequencies as the values.

To solve this problem, you can follow these steps:

1. Create an empty dictionary to store the frequencies of each unique element.
2. Loop through the list and use `collections.defaultdict` to store the frequencies of each unique element.
3. Use `dict()` to return a dictionary with the unique elements of the list as keys and their frequencies as the values.

Your function should return the dictionary with the unique values and their frequencies.

## Example

```py
value_frequencies(['a', 'b', 'a', 'c', 'a', 'a', 'b']) # { 'a': 4, 'b': 2, 'c': 1 }
```

## Summary

In this challenge, you learned how to create a Python function that takes a list as an argument and returns a dictionary with the unique values of the list as keys and their frequencies as the values. This is a useful technique in data analysis and can be used in many different applications.
