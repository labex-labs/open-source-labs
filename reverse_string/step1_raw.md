# Reverse String

Problem: Implement a function to reverse a string (a list of characters), in-place.

## Requirements

- Can we assume the string is ASCII?
  - Yes
  - Note: Unicode strings could require special handling depending on your language
- Since we need to do this in-place, it seems we cannot use the slice operator or the reversed function?
  - Correct
- Since Python string are immutable, can we use a list of characters instead?
  - Yes

## Example Usage

- None -> None
- [''] -> ['']
- ['f', 'o', 'o', ' ', 'b', 'a', 'r'] -> ['r', 'a', 'b', ' ', 'o', 'o', 'f']
