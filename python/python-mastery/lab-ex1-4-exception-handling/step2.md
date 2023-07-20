# Adding Error Handling

When writing programs that process data, it is common to encounter
errors related to bad data (malformed, missing fields, etc.). Modify
your `pcost.py` program to read the data file `portfolio3.dat`
and run it (hint: it should crash).

Modify your function slightly so that it is able to recover from lines
with bad data. For example, the conversion functions `int()` and
`float()` raise a `ValueError` exception if they can't convert the
input. Use `try` and `except` to catch and print a warning message
about lines that can't be parsed. For example:

```
Couldn't parse: 'C - 53.08\n'
Reason: invalid literal for int() with base 10: '-'
Couldn't parse: 'DIS - 34.20\n'
Reason: invalid literal for int() with base 10: '-'
...
```

Try running your program on the `portfolio3.dat` file
again. It should run successfully despite printed warning messages.
