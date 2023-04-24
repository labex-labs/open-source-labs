# Prod Three

## Problem

Given a list of integers, we need to find the highest product of three numbers in the list. The list can contain negative numbers, and there can be duplicate entries in the input. However, we cannot assume that the input is valid, so we need to check for None input. Additionally, there may be less than three integers in the list.

## Requirements

To solve this problem, we need to consider the following requirements:

- The input must be a list of integers.
- The input can contain negative integers.
- The input can contain duplicate entries.
- There may be less than three integers in the list.
- We need to check for None input.
- The solution must fit into memory.

## Example Usage

Here are some examples of how this function can be used:

- None -> TypeError
- Less than three ints -> ValueError
- [5, -2, 3] -> -30
- [5, -2, 3, 1, -1, 4] -> 60
