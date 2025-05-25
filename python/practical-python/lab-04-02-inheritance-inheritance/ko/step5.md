# 기존 메서드 재정의 (Redefining an existing method)

```python
class MyStock(Stock):
    def cost(self):
        return 1.25 * self.shares * self.price
```

사용 예시입니다.

```python
>>> s = MyStock('GOOG', 100, 490.1)
>>> s.cost()
61262.5
>>>
```

새로운 메서드가 이전 메서드를 대체합니다. 다른 메서드들은 영향을 받지 않습니다. 굉장합니다.
