# Sort Dictionary by Key

## Introduction
Dictionaries are an essential data structure in Python. They are used to store data in key-value pairs. However, sometimes it is necessary to sort the dictionary by key. In this challenge, you will be tasked with writing a function that sorts a dictionary by key.

## Problem
Write a function `sort_dict_by_key(d, reverse=False)` that takes a dictionary `d` and returns a new dictionary sorted by key. The function should have an optional parameter `reverse` that defaults to `False`. If `reverse` is `True`, the dictionary should be sorted in reverse order.

## Example
```py
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
sort_dict_by_key(d) # {'five': 5, 'four': 4, 'one': 1, 'three': 3, 'two': 2}
sort_dict_by_key(d, True) # {'two': 2, 'three': 3, 'one': 1, 'four': 4, 'five': 5}
```

## Summary
In this challenge, you were tasked with writing a function that sorts a dictionary by key. You learned how to use the `sorted()` function to sort a list of tuple pairs from the dictionary and convert it back to a dictionary using the `dict()` function. You also learned how to use the `reverse` parameter in `sorted()` to sort the dictionary in reverse order.