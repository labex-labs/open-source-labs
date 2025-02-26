# Атрибут `__slots__`

Вы можете ограничить набор имен атрибутов.

```python
class Stock:
    __slots__ = ('name','_shares','price')
    def __init__(self, name, shares, price):
        self.name = name
     ...
```

Для других атрибутов будет возбуждена ошибка.

```python
>>> s.price = 385.15
>>> s.prices = 410.2
Traceback (most recent call last):
File "<stdin>", line 1, in?
AttributeError: 'Stock' object has no attribute 'prices'
```

Хотя это предотвращает ошибки и ограничивает использование объектов, на самом деле оно используется для повышения производительности и позволяет Python использовать память более эффективно.
