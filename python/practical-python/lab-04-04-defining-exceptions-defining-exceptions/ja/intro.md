# はじめに

ユーザ定義例外はクラスによって定義されます。

```python
class NetworkError(Exception):
    pass
```

**例外は常に `Exception` から継承します。**

通常は空のクラスです。本体には `pass` を使用します。

また、例外の階層構造を作成することもできます。

```python
class AuthenticationError(NetworkError):
     pass

class ProtocolError(NetworkError):
    pass
```
