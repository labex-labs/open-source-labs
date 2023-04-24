# Mult Other Numbers

## Problem

Given a list of integers, we need to find the products of every other integer for each index. For example, if we have a list [1, 2, 3, 4], the output should be [24, 12, 8, 6]. This is because the product of every other integer for index 0 is 2 _ 3 _ 4 = 24, the product of every other integer for index 1 is 1 _ 3 _ 4 = 12, and so on.

However, there are some edge cases that we need to consider. If the input list is empty, the output should also be an empty list. If the input list contains only one element or if the input list contains a zero, the output should be a list of zeros. Additionally, we cannot use division to solve this problem.

## Requirements

To solve this problem, we need to follow these requirements:

- We cannot use division to solve this problem.
- The output should be a list of integers.
- We cannot assume that the inputs are valid, so we need to handle edge cases such as empty lists and lists with only one element or a zero.
- We can assume that the solution fits memory.

## Example Usage

Here are some examples of how this function should behave:

- None -> TypeError
- [] -> []
- [0] -> []
- [0, 1] -> [1, 0]
- [0, 1, 2] -> [2, 0, 0]
- [1, 2, 3, 4] -> [24, 12, 8, 6]
