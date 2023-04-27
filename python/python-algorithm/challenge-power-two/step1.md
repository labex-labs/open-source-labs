# Power Two

## Problem

Write a Python function called `is_power_of_two` that takes in an integer as its parameter and returns `True` if the input is a power of two, and `False` otherwise. A power of two is any number that can be expressed as 2^n, where n is an integer. For example, 2, 4, 8, and 16 are all powers of two.

## Requirements

The `is_power_of_two` function must meet the following requirements:

- The input number must be an integer.
- The function must handle invalid inputs gracefully.
- The output must be a boolean.
- The function must fit within memory constraints.

## Example Usage

Here are some examples of how the `is_power_of_two` function should behave:

- `is_power_of_two(None)` should raise a `TypeError`.
- `is_power_of_two(0)` should return `False`.
- `is_power_of_two(1)` should return `True`.
- `is_power_of_two(2)` should return `True`.
- `is_power_of_two(15)` should return `False`.
- `is_power_of_two(16)` should return `True`.
