# Number is Prime

## Introduction
In mathematics, a prime number is a natural number greater than 1 that is not a product of two smaller natural numbers. For example, 5 is prime because the only ways of writing it as a product, 1 × 5 or 5 × 1, involve 5 itself. However, 4 is not prime because it is a product (2 × 2) in which both numbers are smaller than 4. In this challenge, you need to write a Python function to check if a given number is prime or not.

## Problem
Write a Python function called `is_prime(n)` that takes an integer `n` as input and returns `True` if the number is prime, and `False` otherwise. To solve this problem, you need to follow these rules:

- Return `False` if the number is `0`, `1`, a negative number or a multiple of `2`.
- Use `all()` and `range()` to check numbers from `3` to the square root of the given number.
- Return `True` if none divides the given number, `False` otherwise.

## Example

```py
is_prime(11) # True
```

## Summary
In this challenge, you learned how to check if a given number is prime or not using Python. You used the `all()` and `range()` functions to check numbers from `3` to the square root of the given number. You also learned how to return `True` if none divides the given number, `False` otherwise.