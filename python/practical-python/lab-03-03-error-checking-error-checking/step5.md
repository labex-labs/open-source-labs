# Exception Values

Exceptions have an associated value. It contains more specific information about what's wrong.

```python
raise RuntimeError('Invalid user name')
```

This value is part of the exception instance that's placed in the variable supplied to `except`.

```python
try:
    ...
except RuntimeError as e:   # `e` holds the exception raised
    ...
```

`e` is an instance of the exception type. However, it often looks like a string when printed.

```python
except RuntimeError as e:
    print('Failed : Reason', e)
```
