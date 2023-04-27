# Rotation

## Problem

Given two strings s1 and s2, determine if s1 is a rotation of s2 by calling (only once) a function is_substring. The function is_substring takes two strings as input and returns True if the first string is a substring of the second string, and False otherwise.

## Requirements

To solve this problem, we need to meet the following requirements:

- The string is ASCII.
- The comparison is case sensitive.
- We can use additional data structures.
- The strings can fit in memory.

## Example Usage

Here are some examples of how the function should behave:

- If the strings have different sizes, the function should return False.
- If any of the strings is None, the function should return False.
- If one of the strings is a space and the other is not, the function should return False.
- If both strings are spaces, the function should return True.
- If s1 is a rotation of s2, the function should return True.
