# Pad String

## Introduction
In Python, sometimes we need to pad a string with a specific character to make it a certain length. For example, we may want to pad a string with spaces on both sides to make it a certain length. In this challenge, you will be tasked with writing a function that pads a string on both sides with the specified character, if it's shorter than the specified length.

## Problem
Write a function `pad(s: str, length: int, char: str = ' ') -> str` that pads a string on both sides with the specified character, if it's shorter than the specified length. The function should take in three parameters:
- `s`: a string that needs to be padded
- `length`: an integer that specifies the total length of the padded string
- `char`: a character that is used to pad the string. The default value is a whitespace character.

The function should return the padded string.

## Example
```py
pad('cat', 8) # '  cat   '
pad('42', 6, '0') # '004200'
pad('foobar', 3) # 'foobar'
```

## Summary
In this challenge, you learned how to pad a string on both sides with the specified character, if it's shorter than the specified length. You used the `str.ljust()` and `str.rjust()` methods to pad both sides of the given string. You also learned how to use the whitespace character as the default padding character.