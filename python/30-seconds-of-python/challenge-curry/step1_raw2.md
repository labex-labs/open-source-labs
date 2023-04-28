# Curry Function

## Introduction

In functional programming, currying is a technique of transforming a function that takes multiple arguments into a sequence of functions that each take a single argument. In Python, we can use the `functools.partial()` function to implement currying.

## Problem

Write a function `curry(fn, *args)` that curries a given function `fn`. The function should return a new function that behaves like `fn` with the given arguments, `args`, partially applied.

## Example

```py
add = lambda x, y: x + y
add10 = curry(add, 10)
add10(20) # 30
```

## Summary

In this challenge, you learned how to implement a curry function using `functools.partial()` in Python. The curry function allows you to partially apply arguments to a function and return a new function that takes the remaining arguments.
