# Repeat String

## Introduction

In Python, we can use the `*` operator to repeat a string a certain number of times. This can be useful in many situations, such as when we need to create a string with a specific number of characters or when we need to repeat a certain pattern.

## Problem

Write a function called `repeat_string` that takes two parameters: a string `s` and an integer `n`. The function should return a new string that contains `s` repeated `n` times.

For example, if `s` is `"hello"` and `n` is `3`, the function should return `"hellohellohello"`. If `s` is `"abc"` and `n` is `5`, the function should return `"abcabcabcabcabc"`.

## Example

```py
assert repeat_string("hello", 3) == "hellohellohello"
assert repeat_string("abc", 5) == "abcabcabcabcabc"
assert repeat_string("123", 2) == "123123"
```

## Summary

In this challenge, you learned how to use the `*` operator to repeat a string a certain number of times. You also wrote a function called `repeat_string` that takes a string and an integer as parameters and returns a new string that contains the original string repeated `n` times.
