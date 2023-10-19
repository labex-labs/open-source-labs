# Check Prime

## Problem

Write a Python function that takes an integer as input and returns True if the number is prime, and False otherwise. If the input is not an integer or less than 2, the function should raise an exception.

A number is considered prime if it is only divisible by 1 and itself. For example, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, and 97 are the first 25 prime numbers.

## Requirements

The program should meet the following requirements:

- The function should take an integer as input.
- If the input is not an integer or less than 2, the function should raise an exception.
- The function should return True if the input is a prime number, and False otherwise.
- The program should not consider 1 as a prime number.

## Example Usage

- `check_prime(None)` -> `Exception`
- `check_prime('hello')` -> `Exception`
- `check_prime(1)` -> `False`
- `check_prime(7)` -> `True`
