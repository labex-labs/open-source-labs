# Longest Common Subsequence

## Problem

Given two strings, find the longest common subsequence. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements. For example, "ACE" is a subsequence of "ABCDE" but not of "AEDCA".

## Requirements

To solve this problem, the following requirements must be met:

- The inputs may not be valid, so the program should handle invalid inputs.
- The strings are ASCII.
- The program should be case sensitive.
- A subsequence is a non-contiguous block of characters.
- The program should return a string as a result.
- The program should assume that it fits memory.

## Example Usage

Here are some examples of how the program should behave:

- If str0 or str1 is None, an exception should be raised.
- If str0 or str1 equals 0, an empty string should be returned.
- General case:

```
str0 = 'ABCDEFGHIJ'
str1 = 'FOOBCDBCDE'

result: 'BCDE'
```
