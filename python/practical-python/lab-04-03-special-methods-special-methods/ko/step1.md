# 소개

클래스는 특수 메서드를 정의할 수 있습니다. 이러한 메서드는 Python 인터프리터에 특별한 의미를 갖습니다. 항상 `__`로 시작하고 끝납니다. 예를 들어 `__init__`가 있습니다.

```python
class Stock(object):
    def __init__(self):
        ...
    def __repr__(self):
        ...
```

수십 개의 특수 메서드가 있지만, 몇 가지 특정 예시만 살펴보겠습니다.
