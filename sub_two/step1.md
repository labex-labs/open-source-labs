# Sub Two

## Problem

Write a Python function that takes in two integers as input and returns their difference without using the '+' or '-' sign. The function should handle the following cases:

- If either input is None, the function should raise a TypeError.
- The function should work for both positive and negative integers.

## Requirements

To solve this problem, we need to follow these requirements:

- Check for None input and raise a TypeError if necessary.
- We can assume that the inputs will fit into memory.

## Example Usage

Here are some examples of how the function should behave:

```
sub_two(None, 5) -> TypeError
sub_two(7, 5) -> 2
sub_two(-5, -7) -> 2
sub_two(-5, 7) -> -12
sub_two(5, -7) -> 12
```
