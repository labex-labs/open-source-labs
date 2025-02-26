# Простые атрибуты

Рассмотрим следующий класс.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Поразительным является то, что вы можете устанавливать атрибуты любым значением:

```python
>>> s = Stock('IBM', 50, 91.1)
>>> s.shares = 100
>>> s.shares = "hundred"
>>> s.shares = [1, 0, 0]
>>>
```

Вы, возможно, посмотрите на это и подумаете, что нужны дополнительные проверки.

```python
s.shares = '50'     # Raise a TypeError, this is a string
```

Как бы вы это сделали?
