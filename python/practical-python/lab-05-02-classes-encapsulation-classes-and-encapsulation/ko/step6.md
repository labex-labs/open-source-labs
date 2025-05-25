# 관리형 속성 (Managed Attributes)

한 가지 접근 방식: 접근자 메서드 (accessor methods) 도입.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.set_shares(shares)
        self.price = price

    # Function that layers the "get" operation
    def get_shares(self):
        return self._shares

    # Function that layers the "set" operation
    def set_shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        self._shares = value
```

이것이 기존 코드를 모두 망가뜨린다는 것은 유감입니다. `s.shares = 50`은 `s.set_shares(50)`이 됩니다.
