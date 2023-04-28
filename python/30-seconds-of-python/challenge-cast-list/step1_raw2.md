# Cast to List Challenge

## Introduction

In Python, sometimes we need to convert a value into a list. However, if the value is already a list, we don't want to create a nested list. In this challenge, you will create a function that takes a value and returns it as a list, unless it is already a list or another iterable.

## Problem

Write a function `cast_list(val)` that takes a value as an argument and returns it as a list. If the value is already a list, return it as is. If the value is not a list but is iterable, return it as a list. If the value is not iterable, return it as a single-item list.

## Example

```py
cast_list('foo') # ['foo']
cast_list([1]) # [1]
cast_list(('foo', 'bar')) # ['foo', 'bar']
```

## Summary

In this challenge, you learned how to create a function that casts a value to a list if it is not already a list or another iterable. You used `isinstance()` to check if the value is iterable and returned it using `list()` or encapsulated it in a list accordingly.
