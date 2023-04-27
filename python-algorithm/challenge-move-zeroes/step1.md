# Move Zeroes

## Problem

Given an array of integers, write a function to move all zeroes in the list to the end. The function should do this in-place, meaning it should modify the original list and not create a new one. The ordering of non-zero values should be maintained. The function should handle invalid inputs and assume that the input fits in memory.

## Requirements

To solve this problem, we need to consider the following requirements:

- The input should be an array of integers.
- The output should be the modified input list.
- The function should move all zeroes in the list to the end.
- The function should modify the original list in-place.
- The ordering of non-zero values should be maintained.
- The function should handle invalid inputs.
- The input should fit in memory.

## Example Usage

Here are some examples of how the function should behave:

- None -> TypeError
- [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]
- [1, 0] -> [1, 0]
- [0, 1] -> [1, 0]
- [0] -> [0]
- [1] -> [1]
- [1, 1] -> [1, 1]
