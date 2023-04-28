# Find Keys with Value

## Introduction

Dictionaries are a fundamental data structure in Python. They are used to store key-value pairs, where each key is unique. Sometimes, we need to find all the keys in a dictionary that have a specific value. In this challenge, you will be asked to write a function that finds all the keys in a dictionary that have a given value.

## Problem

Write a Python function called `find_keys(dictionary, value)` that takes in a dictionary and a value as arguments and returns a list of all the keys in the dictionary that have the given value. If there are no keys with the given value, the function should return an empty list.

To solve this problem, you can use the `dictionary.items()` method, which returns a generator that yields key-value pairs of the dictionary. You can then use a list comprehension to filter out the keys that have the given value.

## Example

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 10,
}
find_keys(ages, 10) # [ 'Peter', 'Anna' ]
```

In this example, the `find_keys()` function is called with a dictionary `ages` and a value `10`. The function returns a list of keys that have the value `10`, which are `'Peter'` and `'Anna'`.

## Summary

In this challenge, you have learned how to find all the keys in a dictionary that have a given value. You have written a Python function called `find_keys(dictionary, value)` that takes in a dictionary and a value as arguments and returns a list of all the keys in the dictionary that have the given value. You have used the `dictionary.items()` method and a list comprehension to solve this problem.
