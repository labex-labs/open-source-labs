# `__slots__` 属性

你可以限制属性名称的集合。

```python
class Stock:
    __slots__ = ('name','_shares','price')
    def __init__(self, name, shares, price):
        self.name = name
     ...
```

对于其他属性，它会引发错误。

```python
>>> s.price = 385.15
>>> s.prices = 410.2
Traceback (most recent call last):
File "<stdin>", line 1, in?
AttributeError: 'Stock' object has no attribute 'prices'
```

虽然这可以防止错误并限制对象的使用，但它实际上是用于提高性能，并使 Python 更有效地使用内存。
