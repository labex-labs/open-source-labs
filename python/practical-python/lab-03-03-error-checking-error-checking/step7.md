# Catching All Errors

To catch any exception, use `Exception` like this:

```python
try:
    ...
except Exception:       # DANGER. See below
    print('An error occurred')
```

In general, writing code like that is a bad idea because you'll have no idea why it failed.
