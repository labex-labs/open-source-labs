# 계약 프로그래밍 (Contract Programming)

계약에 의한 설계 (Design By Contract) 라고도 알려진 어서션의 자유로운 사용은 소프트웨어 설계를 위한 접근 방식입니다. 이는 소프트웨어 설계자가 소프트웨어 구성 요소에 대한 정확한 인터페이스 사양을 정의해야 한다고 규정합니다.

예를 들어, 함수의 모든 입력에 어서션을 넣을 수 있습니다.

```python
def add(x, y):
    assert isinstance(x, int), 'Expected int'
    assert isinstance(y, int), 'Expected int'
    return x + y
```

입력을 확인하면 적절한 인수를 사용하지 않는 호출자를 즉시 잡아낼 수 있습니다.

```python
>>> add(2, 3)
5
>>> add('2', '3')
Traceback (most recent call last):
...
AssertionError: Expected int
>>>
```
