# Key of Max Value

## Introduction
In Python, dictionaries are a useful data structure that allows you to store key-value pairs. Sometimes, you may need to find the key of the maximum value in a dictionary. In this challenge, you will write a function that takes a dictionary as an argument and returns the key of the maximum value in the dictionary.

## Problem
Write a function `key_of_max(d)` that takes a dictionary `d` as an argument and returns the key of the maximum value in the dictionary. If there are multiple keys with the same maximum value, return any one of them.

To solve this problem, you can use the `max()` function with the `key` parameter set to `dict.get()`. This will return the key of the maximum value in the dictionary.

## Example
```py
key_of_max({'a':4, 'b':0, 'c':13}) # 'c'
```

## Summary
In this challenge, you learned how to find the key of the maximum value in a dictionary using Python. You can use the `max()` function with the `key` parameter set to `dict.get()` to find and return the key of the maximum value in the given dictionary.