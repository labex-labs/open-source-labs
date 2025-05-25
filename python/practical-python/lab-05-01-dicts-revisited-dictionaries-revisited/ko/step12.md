# 메서드 결정 순서 (Method Resolution Order, MRO)

Python 은 상속 체인을 미리 계산하여 클래스의 `_MRO_` 속성에 저장합니다. 이를 확인할 수 있습니다.

```python
>>> E.__mro__
(<class '__main__.E'>, <class '__main__.D'>,
 <class '__main__.B'>, <class '__main__.A'>,
 <type 'object'>)
>>>
```

이 체인을 **메서드 결정 순서 (Method Resolution Order)**라고 부릅니다. 속성을 찾기 위해 Python 은 MRO 를 순서대로 탐색합니다. 첫 번째 일치하는 항목이 선택됩니다.
