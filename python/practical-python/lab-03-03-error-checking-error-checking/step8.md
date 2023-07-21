# Wrong Way to Catch Errors

Here is the wrong way to use exceptions.

```python
try:
    go_do_something()
except Exception:
    print('Computer says no')
```

This catches all possible errors and it may make it impossible to debug
when the code is failing for some reason you didn't expect at all
(e.g. uninstalled Python module, etc.).
