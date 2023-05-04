# Str Diff

## Problem

Given two strings, we need to find the single different character between them. The strings are assumed to be ASCII and are in lowercase. We cannot assume that the inputs are valid, so we need to check for None. If the inputs are valid, we can assume that there is only a single different character between the two strings. We also need to ensure that the solution fits in memory.

## Requirements

To solve this problem, we need to consider the following requirements:

- The strings are ASCII.
- The strings are in lowercase.
- We need to check for None input.
- There is only a single different character between the two strings.
- The solution should fit in memory.

## Example Usage

Here are some examples of how to use the function:

- None input -> TypeError
- 'ab', 'aab' -> 'a'
- 'aab', 'ab' -> 'a'
- 'abcd', 'abcde' -> 'e'
- 'aaabbcdd', 'abdbacade' -> 'e'
