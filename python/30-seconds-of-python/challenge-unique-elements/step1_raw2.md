# Unique Elements in List

## Introduction
In Python, a list is a collection of items that are ordered and changeable. Sometimes, we need to find the unique elements in a list, which means we want to remove any duplicates and only keep the distinct values. In this challenge, you will write a function that takes a list as input and returns a new list containing only the unique elements.

## Problem
Write a Python function called `unique_elements` that takes a list as input and returns a new list containing only the unique elements. Your function should perform the following steps:
- Create a `set` from the list to discard duplicated values.
- Return a `list` from the set.

Your function should have the following signature:
```python
def unique_elements(li: List) -> List:
```

## Example
```python
assert unique_elements([1, 2, 2, 3, 4, 3]) == [1, 2, 3, 4]
assert unique_elements(['a', 'b', 'c', 'a', 'd']) == ['a', 'b', 'c', 'd']
assert unique_elements([]) == []
```

## Summary
In this challenge, you have written a Python function that takes a list as input and returns a new list containing only the unique elements. You have learned how to use sets to remove duplicates and how to convert a set back to a list.