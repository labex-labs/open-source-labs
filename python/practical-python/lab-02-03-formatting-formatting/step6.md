# Exercise 2.8: How to format numbers

A common problem with printing numbers is specifying the number of
decimal places. One way to fix this is to use f-strings. Try these
examples:

```python
>>> value = 42863.1
>>> print(value)
42863.1
>>> print(f'{value:0.4f}')
42863.1000
>>> print(f'{value:>16.2f}')
        42863.10
>>> print(f'{value:<16.2f}')
42863.10
>>> print(f'{value:*>16,.2f}')
*******42,863.10
>>>
```

Full documentation on the formatting codes used f-strings can be found
[here](https://docs.python.org/3/library/string.html#format-specification-mini-language). Formatting
is also sometimes performed using the `%` operator of strings.

```python
>>> print('%0.4f' % value)
42863.1000
>>> print('%16.2f' % value)
        42863.10
>>>
```

Documentation on various codes used with `%` can be found
[here](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting).

Although it’s commonly used with `print`, string formatting is not tied to printing.
If you want to save a formatted string. Just assign it to a variable.

```python
>>> f = '%0.4f' % value
>>> f
'42863.1000'
>>>
```
