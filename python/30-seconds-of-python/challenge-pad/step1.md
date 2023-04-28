# Pad String

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

