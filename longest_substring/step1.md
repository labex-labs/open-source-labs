# Longest Substring

## Problem

Given two strings, the task is to find the longest common substring. A substring is a contiguous block of characters. The solution should be case-sensitive and assume that the strings are ASCII. The output should be a string and the program should assume that the inputs are not necessarily valid. However, it can assume that the problem fits in memory.

## Requirements

To solve this problem, the program must meet the following requirements:

- The inputs are not necessarily valid.
- The strings are ASCII.
- The solution should be case-sensitive.
- A substring is a contiguous block of characters.
- The output should be a string.
- The program should assume that the problem fits in memory.

## Example Usage

The program should behave as follows:

- If str0 or str1 is None, an exception should be raised.
- If str0 or str1 equals 0, the output should be an empty string.
- In the general case, given str0 = 'ABCDEFGHIJ' and str1 = 'FOOBCDBCDE', the output should be 'BCDE'.
