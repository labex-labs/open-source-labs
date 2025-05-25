# 오버라이딩 (Overriding)

때로는 클래스가 기존 메서드를 확장하지만, 재정의 내에서 원래 구현을 사용하고 싶을 수 있습니다. 이를 위해 `super()`를 사용합니다.

```python
class Stock:
    ...
    def cost(self):
        return self.shares * self.price
    ...

class MyStock(Stock):
    def cost(self):
        # Check the call to `super`
        actual_cost = super().cost()
        return 1.25 * actual_cost
```

`super()`를 사용하여 이전 버전을 호출합니다.

_주의: Python 2 에서는 구문이 더 장황했습니다._

```python
actual_cost = super(MyStock, self).cost()
```
