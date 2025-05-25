# 새로운 메서드 추가 (Add a new method)

```python
class MyStock(Stock):
    def panic(self):
        self.sell(self.shares)
```

사용 예시입니다.

```python
>>> s = MyStock('GOOG', 100, 490.1)
>>> s.sell(25)
>>> s.shares
75
>>> s.panic()
>>> s.shares
0
>>>
```
