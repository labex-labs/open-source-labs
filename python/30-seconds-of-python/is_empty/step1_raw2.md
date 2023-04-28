# Collection is empty

## Introduction

In Python, we often need to check if a sequence or collection is empty. An empty sequence or collection is one that has no elements. In this challenge, you will create a function that checks if a value is an empty sequence or collection.

## Problem

Write a Python function called `is_empty(val)` that takes a value as its parameter and returns `True` if the value is an empty sequence or collection, and `False` otherwise.

To check if a sequence or collection is empty, you can use the `not` operator to test the truth value of the provided sequence or collection. If the sequence or collection is empty, the `not` operator will return `True`.

Your function should be able to handle the following types of sequences and collections:
- Lists
- Tuples
- Sets
- Dictionaries
- Strings
- Ranges

## Example

```python
assert is_empty([]) == True
assert is_empty({}) == True
assert is_empty('') == True
assert is_empty(set()) == True
assert is_empty(range(0)) == True
assert is_empty([1, 2]) == False
assert is_empty({'a': 1, 'b': 2}) == False
assert is_empty('text') == False
assert is_empty(set([1, 2])) == False
assert is_empty(range(2)) == False
```

## Summary

In this challenge, you created a function that checks if a value is an empty sequence or collection. You learned how to use the `not` operator to test the truth value of a sequence or collection and handle different types of sequences and collections.