# String Anagram

Write a function `is_anagram(s1, s2)` that takes two strings as arguments and returns `True` if they are anagrams of each other, and `False` otherwise. The function should be case-insensitive, ignore spaces, punctuation, and special characters.

To solve this problem, you can follow these steps:

1. Use `str.isalnum()` to filter out non-alphanumeric characters and `str.lower()` to transform each character to lowercase.
2. Use `collections.Counter` to count the resulting characters for each string and compare the results.

```python
from collections import Counter

def is_anagram(s1, s2):
  return Counter(
    c.lower() for c in s1 if c.isalnum()
  ) == Counter(
    c.lower() for c in s2 if c.isalnum()
  )
```

```python
is_anagram('#anagram', 'Nag a ram!')  # True
```
