# Einführung

Benutzerdefinierte Ausnahmen werden durch Klassen definiert.

```python
class NetworkError(Exception):
    pass
```

**Ausnahmen erben immer von `Exception`.**

Normalerweise sind es leere Klassen. Verwenden Sie `pass` für den Körper.

Sie können auch eine Hierarchie Ihrer Ausnahmen erstellen.

```python
class AuthenticationError(NetworkError):
     pass

class ProtocolError(NetworkError):
    pass
```
