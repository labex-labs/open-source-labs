# 新しいメソッドを追加する

```python
class MyStock(Stock):
    def panic(self):
        self.sell(self.shares)
```

使用例。

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
