# 예시 (Example)

다음은 시작 클래스라고 가정해 보겠습니다.

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

상속을 통해 이 클래스의 모든 부분을 변경할 수 있습니다.
