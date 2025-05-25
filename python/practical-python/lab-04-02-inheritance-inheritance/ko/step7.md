# `__init__`과 상속 (inheritance)

`__init__`이 재정의된 경우, 부모를 초기화하는 것이 필수적입니다.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        # Check the call to `super` and `__init__`
        super().__init__(name, shares, price)
        self.factor = factor

    def cost(self):
        return self.factor * super().cost()
```

이전에 보여드린 것처럼, 이전 버전을 호출하는 방법인 `super`에서 `__init__()` 메서드를 호출해야 합니다.
