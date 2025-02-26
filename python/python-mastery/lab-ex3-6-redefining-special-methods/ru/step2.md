# Сравнение объектов

Что произойдет, если вы создадите два одинаковых объекта `Stock` и попытаетесь сравнить их? Узнать можно так:

```python
>>> a = Stock('GOOG', 100, 490.1)
>>> b = Stock('GOOG', 100, 490.1)
>>> a == b
False
>>>
```

Вы можете это исправить, создав у класса `Stock` метод `__eq__()`. Например:

```python
class Stock:
  ...
    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                             (other.name, other.shares, other.price))
  ...
```

Примените это изменение и снова попытайтесь сравнить два объекта.
