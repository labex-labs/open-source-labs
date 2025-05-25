# 사전 정의된 데코레이터 (Predefined Decorators)

클래스 정의에서 특별한 종류의 메서드를 지정하는 데 사용되는 사전 정의된 데코레이터가 있습니다.

```python
class Foo:
    def bar(self,a):
        ...

    @staticmethod
    def spam(a):
        ...

    @classmethod
    def grok(cls,a):
        ...

    @property
    def name(self):
        ...
```

하나씩 살펴보겠습니다.
