# 인스턴스 데이터 (Instance Data)

각 인스턴스는 자체 로컬 데이터를 가지고 있습니다.

```python
>>> a.x
2
>>> b.x
10
```

이 데이터는 `__init__()`에 의해 초기화됩니다.

```python
class Player:
    def __init__(self, x, y):
        # `self` 에 저장된 모든 값은 인스턴스 데이터입니다.
        self.x = x
        self.y = y
        self.health = 100
```

저장되는 속성의 총 개수나 유형에 대한 제한은 없습니다.
