# 字典（Dict）与对象（Object）

用户定义的对象（object）同样使用字典（dictionary）来存储实例数据和类数据。实际上，整个对象系统大多是构建在字典之上的一层额外抽象。

字典用于保存实例数据，即 `__dict__`。

```python
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s.__dict__
{'name' : 'GOOG', 'shares' : 100, 'price': 490.1 }
```

当你对 `self` 进行赋值操作时，就会填充这个字典（以及实例）。

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

实例数据 `self.__dict__` 看起来是这样的：

```python
{
    'name': 'GOOG',
    'shares': 100,
    'price': 490.1
}
```

**每个实例都有自己独立的私有字典。**

```python
s = Stock('GOOG', 100, 490.1)     # {'name' : 'GOOG','shares' : 100, 'price': 490.1 }
t = Stock('AAPL', 50, 123.45)     # {'name' : 'AAPL','shares' : 50, 'price': 123.45 }
```

如果你创建了某个类的 100 个实例，就会有 100 个字典用于存储数据。
