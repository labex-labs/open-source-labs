# 类变量与继承

诸如 `types` 这样的类变量有时在使用继承时被用作一种定制机制。例如，在 `Stock` 类中，可以在子类中轻松更改类型。试试这个将 `price` 属性更改为 `Decimal` 实例的示例（`Decimal` 通常更适合财务计算）：

```python
>>> from decimal import Decimal
>>> class DStock(Stock):
        types = (str, int, Decimal)

>>> row = ['AA', '100', '32.20']
>>> s = DStock.from_row(row)
>>> s.price
Decimal('32.20')
>>> s.cost()
Decimal('3220.0')
>>>
```

**设计讨论**

本实验中要解决的问题涉及从文件读取的数据的转换。那么在 `Stock` 类的 `__init__()` 方法中执行这些转换是否有意义呢？例如：

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = str(name)
        self.shares = int(shares)
        self.price = float(price)
```

通过这样做，你可以按如下方式转换一行数据：

```python
>>> row = ['AA', '100', '32.20']
>>> s = Stock(*row)
>>> s.name
'AA'
>>> s.shares
100
>>> s.price
32.2
>>>
```

这是好是坏呢？你有什么想法？总体而言，我认为这是一个有问题的设计，因为它将两件不同的事情混在一起了——实例的创建和数据的转换。此外，`__init__()` 中的隐式转换限制了灵活性，如果用户不小心，可能会引入奇怪的错误。
