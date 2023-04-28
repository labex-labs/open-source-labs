# Apply Function When True

## Introduction
In Python, functions are first-class objects, which means that they can be passed around like any other value. One useful application of this is to conditionally apply a function to a value based on some predicate. In this challenge, you will be asked to write a function that takes a predicate function and a function to apply when the predicate is true, and returns a new function that applies the function when the predicate is true.

## Problem
Write a function called `when` that takes two arguments: a predicate function `predicate` and a function to apply `when_true`. The `when` function should return a new function that takes a single argument `x`. The new function should check if the value of `predicate(x)` is `True`. If it is, the new function should call `when_true(x)` and return the result. Otherwise, the new function should return `x`.

## Example
```py
def double(x):
    return x * 2

def is_even(x):
    return x % 2 == 0

double_even_numbers = when(is_even, double)
double_even_numbers(2) # 4
double_even_numbers(1) # 1
```

## Summary
In this challenge, you have written a function that conditionally applies a function to a value based on some predicate. This is a useful technique for creating more flexible and reusable code.