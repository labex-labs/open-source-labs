# Merge Ranges

## Problem

Given a list of tuples representing ranges, condense the ranges. A range is defined as a tuple of two integers, where the first integer is less than the second integer. The output should be a new list of tuples representing the condensed ranges. If there are no overlapping ranges, the output should be the same as the input.

## Requirements

To solve this problem, the following requirements should be met:

- The tuples may not be in sorted order.
- The tuples must be integers.
- All tuples will have the first element less than the second.
- There is no upper bound on the input range.
- The output should be a list of tuples.
- The output should be a new array.
- The input may be None, in which case a TypeError should be raised.
- The input will fit in memory.

## Example Usage

The following examples demonstrate the expected behavior of the solution:

- None input -> TypeError
- [] -> []
- [(2, 3), (7, 9)] -> [(2, 3), (7, 9)]
- [(2, 3), (3, 5), (7, 9), (8, 10)] -> [(2, 5), (7, 10)]
- [(2, 3), (3, 5), (7, 9), (8, 10), (1, 11)] -> [(1, 11)]
- [(2, 3), (3, 8), (7, 9), (8, 10)] -> [(2, 10)]
