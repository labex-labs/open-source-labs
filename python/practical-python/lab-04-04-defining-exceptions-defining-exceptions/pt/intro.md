# Introdução

Exceções definidas pelo usuário são definidas por classes.

```python
class NetworkError(Exception):
    pass
```

**Exceções sempre herdam de `Exception`.**

Geralmente, elas são classes vazias. Use `pass` para o corpo.

Você também pode criar uma hierarquia de suas exceções.

```python
class AuthenticationError(NetworkError):
     pass

class ProtocolError(NetworkError):
    pass
```
