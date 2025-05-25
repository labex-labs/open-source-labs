# 비공개 속성 (Private Attributes)

선행 `_`가 있는 모든 속성 이름은 _비공개 (private)_ 로 간주됩니다.

```python
class Person(object):
    def __init__(self, name):
        self._name = 0
```

앞서 언급했듯이, 이것은 단지 프로그래밍 스타일일 뿐입니다. 여전히 접근하고 변경할 수 있습니다.

```python
>>> p = Person('Guido')
>>> p._name
'Guido'
>>> p._name = 'Dave'
>>>
```

일반적으로, 선행 `_`가 있는 모든 이름은 변수, 함수 또는 모듈 이름에 관계없이 내부 구현으로 간주됩니다. 이러한 이름을 직접 사용하고 있다면, 아마도 무언가를 잘못하고 있는 것입니다. 더 높은 수준의 기능을 찾아보세요.
