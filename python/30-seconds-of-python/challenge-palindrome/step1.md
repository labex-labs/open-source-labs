# Palindrome

## Problem

Write a function `palindrome(s)` that takes a string `s` as its only parameter and returns `True` if `s` is a palindrome and `False` otherwise. Your function should ignore capitalization and non-alphanumeric characters when checking for palindromes.

To solve this problem, you can follow these steps:

1. Use `str.lower()` to convert the string to lowercase.
2. Use `re.sub()` to remove all non-alphanumeric characters from the string.
3. Compare the resulting string with its reverse using slice notation.

## Example

```python
palindrome('taco cat') # True
palindrome('A man, a plan, a canal: Panama') # True
palindrome('hello world') # False
```
