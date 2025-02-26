# Introduction

Les exceptions définies par l'utilisateur sont définies par des classes.

```python
class NetworkError(Exception):
    pass
```

**Les exceptions héritent toujours de `Exception`.**

Généralement, il s'agit de classes vides. Utilisez `pass` pour le corps.

Vous pouvez également créer une hiérarchie de vos exceptions.

```python
class AuthenticationError(NetworkError):
     pass

class ProtocolError(NetworkError):
    pass
```
