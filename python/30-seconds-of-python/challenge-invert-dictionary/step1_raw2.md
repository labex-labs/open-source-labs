# Invert a Dictionary

## Introduction

A dictionary is a collection of key-value pairs, where each key is unique. In Python, dictionaries are widely used to store and retrieve data efficiently. However, sometimes we need to invert a dictionary, i.e., swap the keys and values. This can be useful in many scenarios, such as searching for a key based on its value. In this challenge, you will write a Python function to invert a dictionary.

## Problem

Write a Python function called `invert_dictionary(obj)` that takes a dictionary `obj` as an argument and returns a new dictionary with the keys and values inverted. The input dictionary `obj` will have unique hashable values. The output dictionary should have the same keys as the input dictionary, but the values should be the keys from the input dictionary.

You should use `dictionary.items()` in combination with a list comprehension to create the new dictionary.

## Example

```py
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
invert_dictionary(ages) # { 10: 'Peter', 11: 'Isabel', 9: 'Anna' }
```

## Summary

In this challenge, you learned how to invert a dictionary in Python. You used `dictionary.items()` in combination with a list comprehension to create a new dictionary with the values and keys inverted. This can be useful in many scenarios, such as searching for a key based on its value.
