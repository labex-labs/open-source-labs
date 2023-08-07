# Reraising an Exception

Use `raise` to propagate a caught error.

```python
try:
    go_do_something()
except Exception as e:
    print('Computer says no. Reason :', e)
    raise
```

This allows you to take action (e.g. logging) and pass the error on to the caller.
