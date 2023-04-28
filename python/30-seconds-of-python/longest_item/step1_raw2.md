# Longest Item

## Introduction

In this challenge, you will write a function that takes any number of iterable objects or objects with a length property and returns the longest one.

## Problem

Write a function `longest_item(*args)` that takes any number of iterable objects or objects with a length property and returns the longest one. The function should:

- Use `max()` with `len()` as the `key` to return the item with the greatest length.
- If multiple items have the same length, the first one will be returned.

## Example

```py
longest_item('this', 'is', 'a', 'testcase') # 'testcase'
longest_item([1, 2, 3], [1, 2], [1, 2, 3, 4, 5]) # [1, 2, 3, 4, 5]
longest_item([1, 2, 3], 'foobar') # 'foobar'
```

## Summary

In this challenge, you learned how to write a function that takes any number of iterable objects or objects with a length property and returns the longest one. You used `max()` with `len()` as the `key` to return the item with the greatest length. If multiple items have the same length, the first one will be returned.