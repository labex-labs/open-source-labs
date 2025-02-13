# Permutations

## Problem

Given an input string, the task is to find all possible permutations of the characters in the string. The output should be a list of strings, where each string represents a unique permutation of the input string. The input string may contain duplicates, but the output should not have any duplicates.

## Requirements

To solve this problem, we need to consider the following requirements:

- The input may contain duplicates.
- The output should not have any duplicates.
- The output should be a list of strings.
- The results do not need to be sorted.
- The inputs may not always be valid.
- The solution should fit in memory.

## Example Usage

Here are some examples of how the function should behave:

- If the input is None, the output should be None.
- If the input is an empty string, the output should be an empty string.
- If the input is 'AABC', the output should be ['AABC', 'AACB', 'ABAC', 'ABCA', 'ACAB', 'ACBA', 'BAAC', 'BACA', 'BCAA', 'CAAB', 'CABA', 'CBAA'].
