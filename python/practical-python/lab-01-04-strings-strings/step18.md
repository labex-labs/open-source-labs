# Commentary

As you start to experiment with the interpreter, you often want to
know more about the operations supported by different objects. For
example, how do you find out what operations are available on a
string?

Depending on your Python environment, you might be able to see a list
of available methods via tab-completion. For example, try typing
this:

```python
>>> s = 'hello world'
>>> s.<tab key>
>>>
```

If hitting tab doesn't do anything, you can fall back to the
builtin-in `dir()` function. For example:

```python
>>> s = 'hello'
>>> dir(s)
['__add__', '__class__', '__contains__', ..., 'find', 'format',
'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace',
'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition',
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase',
'title', 'translate', 'upper', 'zfill']
>>>
```

`dir()` produces a list of all operations that can appear after the `(.)`.
Use the `help()` command to get more information about a specific operation:

```python
>>> help(s.upper)
Help on built-in function upper:

upper(...)
    S.upper() -> string

    Return a copy of the string S converted to uppercase.
>>>
```
