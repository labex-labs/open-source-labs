# Reverse String

## Problem

Implement a function to reverse a string (a list of characters), in-place. This means that the function should modify the original string rather than creating a new one. The function should take a list of characters as input and return the same list with the characters reversed.

To solve this problem, we need to consider a few requirements:

## Requirements

- The string can be assumed to be ASCII.
- Since we need to do this in-place, we cannot use the slice operator or the reversed function.
- Since Python strings are immutable, we can use a list of characters instead.

## Example Usage

Here are some examples of how the function should behave:

- None -> None
- [''] -> ['']
- ['f', 'o', 'o', ' ', 'b', 'a', 'r'] -> ['r', 'a', 'b', ' ', 'o', 'o', 'f']
