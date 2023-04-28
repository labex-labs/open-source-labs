# Byte Size of String

## Introduction

In Python, a string is a sequence of characters. Each character in a string takes up a certain amount of memory. The amount of memory taken up by a string is known as its byte size. In this challenge, you will write a function that takes a string as input and returns its byte size.

## Problem

Write a function `byte_size(s)` that takes a string `s` as input and returns its byte size. The byte size of a string is the number of bytes required to store the string in memory. To calculate the byte size of a string, you need to encode the string using a specific encoding scheme. In this challenge, you will use the UTF-8 encoding scheme.

To calculate the byte size of a string, you can follow these steps:

1. Encode the string using the UTF-8 encoding scheme.
2. Get the length of the encoded string.

Your function should return the length of the encoded string.

## Example

```py
byte_size('😀') # 4
byte_size('Hello World') # 11
```

In the example above, the byte size of the string `'😀'` is 4 because it requires 4 bytes to store the UTF-8 encoded version of the string in memory. The byte size of the string `'Hello World'` is 11 because it requires 11 bytes to store the UTF-8 encoded version of the string in memory.

## Summary

In this challenge, you learned how to calculate the byte size of a string in Python. You wrote a function that takes a string as input and returns its byte size by encoding the string using the UTF-8 encoding scheme and getting the length of the encoded string.
