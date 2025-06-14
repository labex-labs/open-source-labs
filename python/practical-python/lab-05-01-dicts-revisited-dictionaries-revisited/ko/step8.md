# 속성 읽기 (Reading Attributes)

인스턴스에서 속성을 읽는다고 가정해 봅시다.

```python
x = obj.name
```

속성은 두 곳에 존재할 수 있습니다:

- 로컬 인스턴스 딕셔너리.
- 클래스 딕셔너리.

두 딕셔너리 모두 확인해야 합니다. 먼저, 로컬 `__dict__`를 확인합니다. 찾을 수 없으면, `__class__`를 통해 클래스의 `__dict__`를 살펴봅니다.

```python
>>> s = Stock(...)
>>> s.name
'GOOG'
>>> s.cost()
49010.0
>>>
```

이 조회 방식은 *클래스*의 멤버가 모든 인스턴스에 의해 공유되는 방식입니다.
