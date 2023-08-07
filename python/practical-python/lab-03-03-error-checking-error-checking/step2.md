# Exceptions

Exceptions are used to signal errors. To raise an exception yourself, use `raise` statement.

```python
if name not in authorized:
    raise RuntimeError(f'{name} not authorized')
```

To catch an exception use `try-except`.

```python
try:
    authenticate(username)
except RuntimeError as e:
    print(e)
```
