# Dictionary Keys

## Introduction

In Python, a dictionary is a collection of key-value pairs. Each key is unique and is used to access its corresponding value. Sometimes, we may need to extract only the keys from a dictionary. In this challenge, you are tasked with creating a function that takes a flat dictionary as input and returns a list of all its keys.

## Problem

Write a function `keys_only(flat_dict)` that takes a flat dictionary as input and returns a list of all its keys.

To solve this problem, you can follow these steps:

1. Use `dict.keys()` to return the keys in the given dictionary.
2. Return a `list()` of the previous result.

## Example

```py
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
keys_only(ages) # ['Peter', 'Isabel', 'Anna']
```

## Summary

In this challenge, you have learned how to extract only the keys from a dictionary in Python. You can use the `dict.keys()` method to return the keys and then convert the result to a list.
