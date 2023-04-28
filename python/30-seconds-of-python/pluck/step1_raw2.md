# Pluck values from list of dictionaries

## Introduction
In Python, a dictionary is a collection of key-value pairs. Sometimes, we need to extract specific values from a list of dictionaries. In this challenge, you need to write a function that takes a list of dictionaries and a key as input and returns a list of values corresponding to the specified key.

## Problem
Write a function `pluck(lst, key)` that takes a list of dictionaries `lst` and a key `key` as arguments and returns a list of values corresponding to the specified `key`. 

You need to:
- Use a list comprehension and `dict.get()` to get the value of `key` for each dictionary in `lst`.
- The function should return an empty list if the input list is empty or if the specified key is not present in any of the dictionaries.

## Example
```py
simpsons = [
  { 'name': 'lisa', 'age': 8 },
  { 'name': 'homer', 'age': 36 },
  { 'name': 'marge', 'age': 34 },
  { 'name': 'bart', 'age': 10 }
]
print(pluck(simpsons, 'age')) # [8, 36, 34, 10]
```

## Summary
In this challenge, you learned how to extract specific values from a list of dictionaries using a list comprehension and `dict.get()`. You also learned how to handle empty input lists and non-existent keys.