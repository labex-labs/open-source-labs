# 상속의 작동 방식 (How inheritance works)

클래스는 다른 클래스로부터 상속받을 수 있습니다.

```python
class A(B, C):
    ...
```

기본 클래스는 각 클래스에 튜플로 저장됩니다.

```python
>>> A.__bases__
(<class '__main__.B'>, <class '__main__.C'>)
>>>
```

이것은 부모 클래스에 대한 링크를 제공합니다.
