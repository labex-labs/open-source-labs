# Merge Dictionaries

## Introduction

In Python, dictionaries are used to store key-value pairs. Sometimes, we may need to combine two or more dictionaries into a single dictionary. In this challenge, you will be asked to write a function that merges two or more dictionaries.

## Problem

Write a function `merge_dictionaries(*dicts)` that takes in two or more dictionaries as arguments and returns a new dictionary that contains all the key-value pairs from the input dictionaries.

Your function should create a new dictionary and loop over the input dictionaries, using `dictionary.update()` to add the key-value pairs from each one to the result.

## Example

```py
ages_one = {
  'Peter': 10,
  'Isabel': 11,
}
ages_two = {
  'Anna': 9
}
merge_dictionaries(ages_one, ages_two)
# { 'Peter': 10, 'Isabel': 11, 'Anna': 9 }
```

## Summary

In this challenge, you have learned how to merge two or more dictionaries in Python. By using the `update()` method, you can easily combine the key-value pairs from multiple dictionaries into a single dictionary.
