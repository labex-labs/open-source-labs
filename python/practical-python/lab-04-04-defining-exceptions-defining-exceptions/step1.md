# Exercise 4.11: Defining a custom exception

It is often good practice for libraries to define their own exceptions.

This makes it easier to distinguish between Python exceptions raised in response to common programming errors versus exceptions intentionally raised by a library to a signal a specific usage problem.

Modify the `create_formatter()` function from the last exercise so that it raises a custom `FormatError` exception when the user provides a bad format name.

For example:

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('xls')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "tableformat.py", line 80, in create_formatter
    raise FormatError(f"Unknown table format {name}")
tableformat.FormatError: Unknown table format xls
>>>
```  
