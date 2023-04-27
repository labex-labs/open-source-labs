# Permutation

## Problem

Given two strings, we need to determine if one string is a permutation of the other. A permutation is defined as a rearrangement of the characters in a string. For example, "act" is a permutation of "cat".

## Requirements

To solve this problem, we need to consider the following requirements:

- The string is ASCII.
- Whitespace is important.
- The comparison is case-sensitive. For example, "Nib" and "bin" are not a match.
- We can use additional data structures.
- We can assume that the strings fit in memory.

## Example Usage

Here are some examples of how this function can be used:

- One or more None inputs -> False
- One or more empty strings -> False
- 'Nib', 'bin' -> False
- 'act', 'cat' -> True
- 'a ct', 'ca t' -> True
