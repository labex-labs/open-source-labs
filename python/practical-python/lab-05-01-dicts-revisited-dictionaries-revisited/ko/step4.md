# 클래스 멤버

별도의 딕셔너리는 또한 메서드를 저장합니다.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

딕셔너리는 `Stock.__dict__`에 있습니다.

```python
{
    'cost': <function>,
    'sell': <function>,
    '__init__': <function>
}
```
