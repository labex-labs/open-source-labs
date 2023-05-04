# String Anagram Challenge

## Introduction

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase. For example, "listen" is an anagram of "silent". In this challenge, you will be asked to write a function that checks if two strings are anagrams of each other.

## Problem

Write a function `is_anagram(s1, s2)` that takes two strings as arguments and returns `True` if they are anagrams of each other, and `False` otherwise. The function should be case-insensitive, ignore spaces, punctuation, and special characters.

To solve this problem, you can follow these steps:

1. Use `str.isalnum()` to filter out non-alphanumeric characters and `str.lower()` to transform each character to lowercase.
2. Use `collections.Counter` to count the resulting characters for each string and compare the results.

## Example

```python
is_anagram('#anagram', 'Nag a ram!')  # True
is_anagram('hello', 'world')  # False
```

## Summary

In this challenge, you have learned how to check if two strings are anagrams of each other. You have used `str.isalnum()` to filter out non-alphanumeric characters, `str.lower()` to transform each character to lowercase, and `collections.Counter` to count the resulting characters for each string and compare the results.
