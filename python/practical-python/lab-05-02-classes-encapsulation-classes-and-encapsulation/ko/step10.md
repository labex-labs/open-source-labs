# `__slots__` 속성 (Attribute)

속성 이름의 집합을 제한할 수 있습니다.

```python
class Stock:
    __slots__ = ('name','_shares','price')
    def __init__(self, name, shares, price):
        self.name = name
        ...
```

다른 속성에 대해서는 오류를 발생시킵니다.

```python
>>> s.price = 385.15
>>> s.prices = 410.2
Traceback (most recent call last):
File "<stdin>", line 1, in ?
AttributeError: 'Stock' object has no attribute 'prices'
```

이것은 오류를 방지하고 객체의 사용을 제한하지만, 실제로 성능을 위해 사용되며 Python 이 메모리를 더 효율적으로 사용하도록 만듭니다.
