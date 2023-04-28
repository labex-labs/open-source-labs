# Dictionary Values

## Introduction

Dictionaries are a fundamental data structure in Python. They allow you to store key-value pairs and are often used to represent real-world objects or concepts. In this challenge, you will be working with dictionaries and their values.

## Problem

You are given a flat dictionary, and you need to create a function that returns a flat list of all the values in the dictionary. Your task is to implement the `values_only(flat_dict)` function, which takes a flat dictionary as an argument and returns a list of all the values in the dictionary.

To solve this problem, you can use the `dict.values()` method to return the values in the given dictionary. Then, you can convert the result to a list using the `list()` function.

## Example

```py
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
values_only(ages) # [10, 11, 9]
```

## Summary

In this challenge, you learned how to extract all the values from a flat dictionary and return them as a list. You used the `dict.values()` method to get the values and then converted the result to a list using the `list()` function. This is a useful technique when working with dictionaries in Python.