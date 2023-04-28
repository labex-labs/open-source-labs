# Pad Number

## Introduction
In Python, sometimes we need to pad a number with leading zeros to make it a certain length. For example, we might want to pad the number `7` to be `000007`. In this challenge, you will need to write a function that pads a given number to the specified length.

## Problem
Write a function `pad_number(n, l)` that takes in a number `n` and a length `l` and returns a string that represents the padded number. The function should pad the number with leading zeros to make it `l` digits long. If the number is already `l` digits long, the function should return the number as a string.

To pad the number, you can use the `str.zfill()` method. This method takes in a length and pads the string with leading zeros until it is that length. For example, `"7".zfill(6)` would return `"000007"`.

## Example
```py
pad_number(1234, 6) # '001234'
pad_number(7, 6) # '000007'
pad_number(123456789, 9) # '123456789'
```

## Summary
In this challenge, you wrote a function that pads a given number to the specified length. You learned how to use the `str.zfill()` method to pad a string with leading zeros.