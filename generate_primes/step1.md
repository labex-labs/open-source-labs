# Generate Primes

## Problem

Write a Python function that generates a list of prime numbers. The function should take an integer as input and return a list of Boolean values, where each value corresponds to whether the index is a prime number or not. For example, if the input is 20, the output should be [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True], where the value at index 2 is True because 2 is a prime number, and the value at index 4 is False because 4 is not a prime number.

## Requirements

- The function should not consider 1 as a prime number.
- The function should handle invalid inputs by raising an exception.
- The function should generate the list of prime numbers in memory.

## Example Usage

- None -> Exception
- Not an int -> Exception
- 20 -> [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True]
