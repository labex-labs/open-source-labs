# Hex to RGB Conversion

Write a function `hex_to_rgb(hex_code)` that takes a hexadecimal color code as a string and returns a tuple of integers corresponding to its RGB components. The function should perform the following steps:

1. Use a list comprehension in combination with `int()` and list slice notation to get the RGB components from the hexadecimal string.
2. Use `tuple()` to convert the resulting list to a tuple.

```python
def hex_to_rgb(hex):
  return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
```

```python
hex_to_rgb('FFA501') # (255, 165, 1)
```
