# Key of Min Value

## Introduction

In Python, dictionaries are a useful data structure for storing key-value pairs. Sometimes, we may need to find the key of the minimum value in a dictionary. In this challenge, you will be tasked with writing a function that finds the key of the minimum value in a given dictionary.

## Problem

Write a function `key_of_min(d)` that takes in a dictionary `d` as its argument and returns the key of the minimum value in the dictionary.

To solve this problem, you can use the built-in `min()` function with the `key` parameter set to `dict.get()`. This will return the key of the minimum value in the dictionary.

## Example

```python
key_of_min({'a':4, 'b':0, 'c':13}) # 'b'
```

In this example, the dictionary `{'a':4, 'b':0, 'c':13}` is passed as an argument to the `key_of_min()` function. The function returns the key `'b'`, which corresponds to the minimum value in the dictionary.

## Summary

In this challenge, you learned how to find the key of the minimum value in a dictionary using Python. By using the `min()` function with the `key` parameter set to `dict.get()`, you can easily find the key of the minimum value in a given dictionary.
