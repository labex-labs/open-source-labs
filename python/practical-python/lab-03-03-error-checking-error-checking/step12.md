# `finally` statement

It specifies code that must run regardless of whether or not an
exception occurs.

```python
lock = Lock()
...
lock.acquire()
try:
    ...
finally:
    lock.release()  # this will ALWAYS be executed. With and without exception.
```

Commonly used to safely manage resources (especially locks, files, etc.).
