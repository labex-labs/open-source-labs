# Digitize Number

## Introduction
In Python, it is often necessary to convert a number into a list of its digits. This can be useful for various applications, such as performing mathematical operations on individual digits or manipulating numbers in a more granular way. In this challenge, you will be tasked with writing a function that takes a number as input and returns a list of its digits.

## Problem
Write a function `digitize(n)` that takes a non-negative integer `n` as input and returns a list of its digits. The function should accomplish this by performing the following steps:

1. Convert the input number `n` to a string.
2. Use the `map()` function combined with the `int` function to convert each character in the string to an integer.
3. Return the resulting list of integers.

For example, if the input number is `123`, the function should return the list `[1, 2, 3]`.

## Example
```python
assert digitize(123) == [1, 2, 3]
assert digitize(4567) == [4, 5, 6, 7]
assert digitize(0) == [0]
```

## Summary
In this challenge, you have learned how to convert a number into a list of its digits using Python. By using the `map()` function and the `int` function, you can easily convert each character in a string to an integer and return a list of those integers. This technique can be useful for various applications, such as performing mathematical operations on individual digits or manipulating numbers in a more granular way.