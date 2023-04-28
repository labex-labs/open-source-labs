# Check if Key Exists in Dictionary

## Introduction
In Python, a dictionary is a collection of key-value pairs. Each key is unique and is used to access its corresponding value. In this challenge, you will write a function that checks if a given key exists in a dictionary.

## Problem
Write a function `key_in_dict(d, key)` that takes a dictionary `d` and a key `key` as arguments and returns `True` if the key exists in the dictionary, `False` otherwise.

## Example
```py
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
key_in_dict(d, 'three') # True
key_in_dict(d, 'six') # False
```

## Summary
In this challenge, you learned how to check if a key exists in a dictionary in Python. You can use the `in` operator to check if a dictionary contains a specific key.