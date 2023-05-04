# RGB to Hex Conversion

Write a function `rgb_to_hex(r, g, b)` that takes in three integers representing the values of the red, green, and blue components of a color, and returns a string representing the hexadecimal color code. The output string should be in the format `RRGGBB`, where `RR`, `GG`, and `BB` are two-digit hexadecimal values representing the red, green, and blue components respectively.

For example, if the input values are `255`, `165`, and `1`, the output should be the string `'FFA501'`.

```py
def rgb_to_hex(r, g, b):
  return ('{:02X}' * 3).format(r, g, b)
```

```py
rgb_to_hex(255, 165, 1) # 'FFA501'
```
