# 소개

사용자 정의 예외는 클래스로 정의됩니다.

```python
class NetworkError(Exception):
    pass
```

**예외는 항상 `Exception`에서 상속됩니다.**

일반적으로 빈 클래스입니다. 본문에는 `pass`를 사용합니다.

예외의 계층 구조를 만들 수도 있습니다.

```python
class AuthenticationError(NetworkError):
     pass

class ProtocolError(NetworkError):
    pass
```
