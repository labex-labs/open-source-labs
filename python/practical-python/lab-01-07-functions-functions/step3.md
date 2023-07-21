# Errors and exceptions

Functions report errors as exceptions. An exception causes a function to abort and may
cause your entire program to stop if unhandled.

Try this in your python REPL.

```python
>>> int('N/A')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'N/A'
>>>
```

For debugging purposes, the message describes what happened, where the error occurred,
and a traceback showing the other function calls that led to the failure.
