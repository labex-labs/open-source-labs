# Palindrome

## Introduction
A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward. For example, "racecar" is a palindrome because when you reverse the word, it still spells "racecar". In this challenge, you will write a function that checks if a given string is a palindrome.

## Problem
Write a function `palindrome(s)` that takes a string `s` as its only parameter and returns `True` if `s` is a palindrome and `False` otherwise. Your function should ignore capitalization and non-alphanumeric characters when checking for palindromes.

To solve this problem, you can follow these steps:
1. Use `str.lower()` to convert the string to lowercase.
2. Use `re.sub()` to remove all non-alphanumeric characters from the string.
3. Compare the resulting string with its reverse using slice notation.

## Example
```py
palindrome('taco cat') # True
palindrome('A man, a plan, a canal: Panama') # True
palindrome('hello world') # False
```

## Summary
In this challenge, you learned how to check if a given string is a palindrome. You used `str.lower()` and `re.sub()` to convert the string to lowercase and remove non-alphanumeric characters, and then compared the resulting string with its reverse using slice notation.