# Свойства

Есть альтернативный подход к предыдущему паттерну.

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

Теперь обычный доступ к атрибуту запускает методы getter и setter, расположенные под `@property` и `@shares.setter`.

```python
>>> s = Stock('IBM', 50, 91.1)
>>> s.shares         # Triggers @property
50
>>> s.shares = 75    # Triggers @shares.setter
>>>
```

При этом паттерне изменения в исходном коде не требуются. Новый _setter_ также вызывается при присваивании внутри класса, включая внутри метода `__init__()`.

```python
class Stock:
    def __init__(self, name, shares, price):
     ...
        # This assignment calls the setter below
        self.shares = shares
     ...

 ...
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
```

Часто возникает путаница между свойством и использованием приватных имен. Хотя свойство внутри использует приватное имя, такое как `_shares`, остальная часть класса (не свойство) может продолжать использовать имя, такое как `shares`.

Свойства также полезны для вычисляемых атрибутов данных.

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

Это позволяет избежать дополнительных круглых скобок, скрывая то, что на самом деле это метод:

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.shares # Instance variable
100
>>> s.cost   # Computed Value
49010.0
>>>
```
