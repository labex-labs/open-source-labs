# String Mutability

Strings are "immutable" or read-only.
Once created, the value can't be changed.

```python
>>> s = 'Hello World'
>>> s[1] = 'a'
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>
```

**All operations and methods that manipulate string data, always create new strings.**
