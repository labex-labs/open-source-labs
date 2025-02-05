# 属性

对于前面的模式，还有另一种方法。

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
```

现在，普通的属性访问会触发 `@property` 和 `@shares.setter` 下的 getter 和 setter 方法。

```python
>>> s = Stock('IBM', 50, 91.1)
>>> s.shares         # 触发 @property
50
>>> s.shares = 75    # 触发 @shares.setter
>>>
```

使用这种模式，无需对源代码进行任何更改。当在类内部进行赋值时，包括在 `__init__()` 方法内部，新的 **setter** 也会被调用。

```python
class Stock:
    def __init__(self, name, shares, price):
     ...
        # 此赋值会调用下面的 setter
        self.shares = shares
     ...

  ...
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
```

属性和使用私有名称之间常常存在混淆。虽然属性在内部使用像 `_shares` 这样的私有名称，但类的其他部分（不是属性本身）可以继续使用像 `shares` 这样的名称。

属性对于计算数据属性也很有用。

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price
  ...
```

这使你可以省略额外的括号，隐藏它实际上是一个方法的事实：

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.shares # 实例变量
100
>>> s.cost   # 计算值
49010.0
>>>
```
