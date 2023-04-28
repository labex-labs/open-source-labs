# Hex to RGB Conversion

## Introduction

In web development, colors are often represented in hexadecimal format, which consists of a pound sign (#) followed by six characters representing the red, green, and blue (RGB) components of the color. However, sometimes we need to convert these hexadecimal color codes to RGB values to use them in other contexts.

## Problem

Write a function `hex_to_rgb(hex_code)` that takes a hexadecimal color code as a string and returns a tuple of integers corresponding to its RGB components. The function should perform the following steps:

1. Use a list comprehension in combination with `int()` and list slice notation to get the RGB components from the hexadecimal string.
2. Use `tuple()` to convert the resulting list to a tuple.

## Example

```py
hex_to_rgb('FFA501') # (255, 165, 1)
```

## Summary

In this challenge, you learned how to convert a hexadecimal color code to its corresponding RGB components using Python. This is a useful skill to have when working with colors in web development or other contexts.
