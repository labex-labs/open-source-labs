# 定义一个简单对象

创建一个名为 `stock.py` 的文件，并定义以下类：

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price
```

完成上述操作后，运行你的程序，并对你新创建的 `Stock` 对象进行实验：

注意：要做到这一点，你可能需要使用 `-i` 选项来运行 Python。例如：

```bash
python3 -i stock.py
```

```python
>>> s = Stock('GOOG',100,490.10)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
>>> s.cost()
49010.0
>>> print('%10s %10d %10.2f' % (s.name, s.shares, s.price))
      GOOG        100     490.10
>>> t = Stock('IBM', 50, 91.5)
>>> t.cost()
4575.0
>>>
```
