# Introduction

User defined exceptions are defined by classes.

```python
class NetworkError(Exception):
    pass
```

**Exceptions always inherit from `Exception`.**

Usually they are empty classes. Use `pass` for the body.

You can also make a hierarchy of your exceptions.

```python
class AuthenticationError(NetworkError):
     pass

class ProtocolError(NetworkError):
    pass
```
