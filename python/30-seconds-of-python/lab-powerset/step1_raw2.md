# Powerset Challenge

## Introduction

In mathematics, the power set of a set is the set of all subsets of the set, including the empty set and the set itself. In Python, we can create a function that returns the powerset of a given iterable.

## Problem

Write a Python function called `powerset(iterable)` that takes an iterable as an argument and returns the powerset of the iterable. The function should follow these steps:

1. Convert the given value to a list.
2. Use `range()` and `itertools.combinations()` to create a generator that returns all subsets.
3. Use `itertools.chain.from_iterable()` and `list()` to consume the generator and return a list.

## Example

```py
powerset([1, 2]) # [(), (1,), (2,), (1, 2)]
```

## Summary

In this challenge, you have learned how to create a Python function that returns the powerset of a given iterable. The function uses `range()` and `itertools.combinations()` to create a generator that returns all subsets, and `itertools.chain.from_iterable()` and `list()` to consume the generator and return a list.
