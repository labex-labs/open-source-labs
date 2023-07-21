# `with` statement

In modern code, `try-finally` is often replaced with the `with` statement.

```python
lock = Lock()
with lock:
    # lock acquired
    ...
# lock released
```

A more familiar example:

```python
with open(filename) as f:
    # Use the file
    ...
# File closed
```

`with` defines a usage _context_ for a resource. When execution
leaves that context, resources are released. `with` only works with
certain objects that have been specifically programmed to support it.
