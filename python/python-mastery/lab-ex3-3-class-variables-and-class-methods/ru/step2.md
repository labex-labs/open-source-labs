# Альтернативные конструкторы

Вероятно, создание объекта `Stock` из строки исходных данных лучше обрабатывать с использованием альтернативного конструктора. Измените класс `Stock` так, чтобы он имел переменную класса `types` и метод класса `from_row()` следующим образом:

```python
class Stock:
    types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)
  ...
```

Вот, как это можно протестировать:

```python
>>> row = ['AA', '100', '32.20']
>>> s = Stock.from_row(row)
>>> s.name
'AA'
>>> s.shares
100
>>> s.price
32.2
>>> s.cost()
3220.0000000000005
>>>
```

Обратите внимание, как строковые значения в строке были преобразованы в соответствующий тип.
