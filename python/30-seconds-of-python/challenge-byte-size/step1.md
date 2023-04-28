# Byte Size of String

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
