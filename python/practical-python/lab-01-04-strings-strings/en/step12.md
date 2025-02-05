# Exercise 1.13: Extracting individual characters and substrings

Strings are arrays of characters. Try extracting a few characters:

```python
>>> symbols[0]
?
>>> symbols[1]
?
>>> symbols[2]
?
>>> symbols[-1]        # Last character
?
>>> symbols[-2]        # Negative indices are from end of string
?
>>>
```

In Python, strings are read-only.

Verify this by trying to change the first character of `symbols` to a lower-case 'a'.

```python
>>> symbols[0] = 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>
```
