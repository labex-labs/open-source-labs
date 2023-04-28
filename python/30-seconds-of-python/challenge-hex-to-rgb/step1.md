# Hex to RGB Conversion

## Problem

Write a function `hex_to_rgb(hex_code)` that takes a hexadecimal color code as a string and returns a tuple of integers corresponding to its RGB components. The function should perform the following steps:

1. Use a list comprehension in combination with `int()` and list slice notation to get the RGB components from the hexadecimal string.
2. Use `tuple()` to convert the resulting list to a tuple.

## Example

```py
hex_to_rgb('FFA501') # (255, 165, 1)
```
