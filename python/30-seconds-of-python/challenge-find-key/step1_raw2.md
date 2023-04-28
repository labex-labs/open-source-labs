# Find the Key of a Value in a Dictionary

## Introduction
Dictionaries are a powerful data structure in Python that allow you to store key-value pairs. Sometimes, you may need to find the key associated with a particular value in a dictionary. In this challenge, you will write a function that takes a dictionary and a value as input, and returns the first key in the dictionary that has the given value.

## Problem
Write a function `find_key(dict, val)` that finds the first key in the provided dictionary that has the given value.

Your function should:
- Take a dictionary `dict` and a value `val` as input.
- Use `dictionary.items()` and `next()` to return the first key that has a value equal to `val`.
- Return the key as output.

## Example
```py
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
find_key(ages, 11) # 'Isabel'
```

## Summary
In this challenge, you learned how to find the key associated with a particular value in a dictionary. You used the `dictionary.items()` method to iterate over the key-value pairs in the dictionary, and the `next()` function to return the first key that has a value equal to the input value.