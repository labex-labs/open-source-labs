# 简介

用户定义的异常是通过类来定义的。

```python
class NetworkError(Exception):
    pass
```

**异常总是继承自 `Exception`。**

通常它们是空类。在类体中使用 `pass`。

你也可以创建异常层次结构。

```python
class AuthenticationError(NetworkError):
     pass

class ProtocolError(NetworkError):
    pass
```
