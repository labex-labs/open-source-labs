# `__slots__` 属性

属性名のセットを制限することができます。

```python
class Stock:
    __slots__ = ('name','_shares','price')
    def __init__(self, name, shares, price):
        self.name = name
     ...
```

他の属性に対してはエラーが発生します。

```python
>>> s.price = 385.15
>>> s.prices = 410.2
Traceback (most recent call last):
File "<stdin>", line 1, in?
AttributeError: 'Stock' object has no attribute 'prices'
```

これはエラーを防ぎ、オブジェクトの使用を制限しますが、実際にはパフォーマンス向上のために使用され、Python がメモリをより効率的に使用するようになります。
