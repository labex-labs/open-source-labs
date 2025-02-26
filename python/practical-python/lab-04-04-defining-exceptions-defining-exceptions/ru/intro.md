# Введение

Пользовательские исключения определяются классами.

```python
class NetworkError(Exception):
    pass
```

**Исключения всегда наследуются от `Exception`.**

Обычно они являются пустыми классами. Используйте `pass` для тела класса.

Вы также можете создать иерархию своих исключений.

```python
class AuthenticationError(NetworkError):
     pass

class ProtocolError(NetworkError):
    pass
```
