# Introducción

Las excepciones definidas por el usuario se definen mediante clases.

```python
class NetworkError(Exception):
    pass
```

**Las excepciones siempre heredan de `Exception`.**

Por lo general, son clases vacías. Utilice `pass` para el cuerpo.

También puede crear una jerarquía de sus excepciones.

```python
class AuthenticationError(NetworkError):
     pass

class ProtocolError(NetworkError):
    pass
```
