# Lists to Dictionary

## Introduction
In Python, a dictionary is a collection of key-value pairs. Sometimes, we may have two separate lists, one containing the keys and the other containing the values, and we want to combine them into a dictionary. In this challenge, you will write a function that takes two lists as input and returns a dictionary where the elements of the first list serve as the keys and the elements of the second list serve as the values.

## Problem
Write a function `to_dictionary(keys, values)` that takes two lists as input and returns a dictionary where the elements of the first list serve as the keys and the elements of the second list serve as the values. The function should use `zip()` in combination with `dict()` to combine the values of the two lists into a dictionary. The function should return `None` if the length of the two lists is not equal.

## Example
```py
to_dictionary(['a', 'b'], [1, 2]) # { 'a': 1, 'b': 2 }
to_dictionary(['a', 'b', 'c'], [1, 2]) # None
```

## Summary
In this challenge, you have learned how to combine two lists into a dictionary using `zip()` and `dict()`. You have also learned how to handle the case where the length of the two lists is not equal.