# 重新定义现有方法

```python
class MyStock(Stock):
    def cost(self):
        return 1.25 * self.shares * self.price
```

使用示例。

```python
>>> s = MyStock('GOOG', 100, 490.1)
>>> s.cost()
61262.5
>>>
```

新方法取代了旧方法。其他方法不受影响。这太棒了。
