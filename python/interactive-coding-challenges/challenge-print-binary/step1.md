# Print Binary

## Problem

Write a Python function that takes a real number between 0 and 1 as input and returns its binary representation as a string. If the length of the representation is greater than 32, return 'ERROR'.

## Requirements

To solve this problem, we need to ensure the following requirements:

- The input must be a float.
- The output must be a string.
- The range of the input is between 0 and 1, but the values 0 and 1 are not inclusive.
- The result must include a trailing zero and decimal point.
- The leading zero and decimal point are counted in the 32 character limit.
- We cannot assume that the inputs are valid.
- We can assume that the program fits in memory.

## Example Usage

Here are some examples of how the function should behave:

- None -> 'ERROR'
- Out of bounds (0, 1) -> 'ERROR'
- 0.625 -> 0.101
- 0.987654321 -> 'ERROR'
