# Dictionary to List

## Introduction
In Python, a dictionary is a collection of key-value pairs. Sometimes, we may need to convert a dictionary to a list of tuples. In this challenge, you are tasked with writing a function that takes a dictionary as an argument and returns a list of tuples.

## Problem
Write a function `dict_to_list(d)` that takes a dictionary `d` as an argument and returns a list of tuples. Each tuple should contain a key-value pair from the dictionary. The order of the tuples in the list should be the same as the order of the key-value pairs in the dictionary.

## Example
```py
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
dict_to_list(d)
# [('one', 1), ('three', 3), ('five', 5), ('two', 2), ('four', 4)]
```

## Summary
In this challenge, you learned how to convert a dictionary to a list of tuples in Python. You can use the `dict.items()` method to get a list of tuples from the dictionary.