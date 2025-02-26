# 既存のメソッドを再定義する

```python
class MyStock(Stock):
    def cost(self):
        return 1.25 * self.shares * self.price
```

使用例。

```python
>>> s = MyStock('GOOG', 100, 490.1)
>>> s.cost()
61262.5
>>>
```

新しいメソッドは古いメソッドの代わりを果たします。他のメソッドは影響を受けません。すごいですね。
