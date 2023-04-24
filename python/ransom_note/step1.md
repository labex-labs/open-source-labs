# Ransom Note

## Problem

We need to create a Python function that takes in two strings as arguments: `magazine` and `note`. The function should return `True` if the ransom note could have been written using the letters in the magazine, and `False` otherwise.

## Requirements

To solve this problem, we need to keep in mind the following requirements:

- The case is sensitive.
- We are working with ASCII characters.
- We can scan the entire magazine.
- The inputs are not necessarily valid.
- The problem fits memory.

## Example Usage

Here are some examples of how the function should behave:

- None -> Exception
- '', '' -> Exception
- 'a', 'b' -> False
- 'aa', 'ab' -> False
- 'aa', 'aab' -> True
