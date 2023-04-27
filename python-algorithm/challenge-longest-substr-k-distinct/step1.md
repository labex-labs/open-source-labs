# Longest Substr K Distinct

## Problem

Given a string and an integer k, find the length of the longest substring that contains at most k distinct characters. A substring is a contiguous block of characters. For example, in the string "abcabcdefgghiij", the longest substring with at most 3 distinct characters is "abcabc". If there are multiple substrings with the same length, return any of them.

## Requirements

To solve this challenge, the following requirements must be met:

- The inputs may not be valid, so the code should handle invalid inputs gracefully.
- The strings are ASCII.
- The search is case sensitive.
- A substring is a contiguous block of characters.
- The result should be an integer.
- The code should be able to handle the input within memory limits.

## Example Usage

The following examples demonstrate the expected behavior of the code:

- None -> TypeError
- '', k = 3 -> 0
- 'abcabcdefgghiij', k=3 -> 6
- 'abcabcdefgghighij', k=3 -> 7
