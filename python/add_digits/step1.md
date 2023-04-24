# Add Digits

## Problem

Given an integer, we need to repeatedly add its digits until the result is a single digit. For example, if we are given the integer 138, we add 1 + 3 + 8 = 12. Since 12 is not a single digit, we repeat the process and add 1 + 2 = 3. Therefore, the final result is 3.

## Requirements

To solve this problem, we need to consider the following requirements:

- The input integer is not negative.
- The inputs may not always be valid, so we need to handle any errors that may occur.
- The solution should fit into memory.

## Example Usage

Here are some examples of how this function can be used:

- If we pass None as input, the function should raise a TypeError.
- If we pass a negative integer as input, the function should raise a ValueError.
- If we pass 9 as input, the function should return 9 since it is already a single digit.
- If we pass 138 as input, the function should return 3.
- If we pass 65536 as input, the function should return 7.
