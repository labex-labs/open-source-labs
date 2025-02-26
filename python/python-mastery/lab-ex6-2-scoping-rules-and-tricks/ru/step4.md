# Собираем все вместе

Взяв идеи из первых двух частей, удалите метод `__init__()`, который был изначально частью класса `Structure`. Затем добавьте метод `_init()` следующим образом:

```python
# structure.py
import sys

class Structure:
  ...
    @staticmethod
    def _init():
        locs = sys._getframe(1).f_locals
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)
  ...
```

Примечание: Причина, по которой это определено как `@staticmethod`, заключается в том, что аргумент `self` получается из локальных переменных - дополнительно не нужно передавать его в качестве аргумента к самому методу (да承认, это немного тонко).

Теперь модифицируйте класс `Stock` так, чтобы он выглядел следующим образом:

```python
# stock.py
from structure import Structure

class Stock(Structure):
    _fields = ('name','shares','price')
    def __init__(self, name, shares, price):
        self._init()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= shares
```

Проверьте, что класс работает правильно, поддерживает аргументы по ключевым словам и имеет правильную сигнатуру помощи.

```python
>>> s = Stock(name='GOOG', price=490.1, shares=50)
>>> s.name
'GOOG'
>>> s.shares
50
>>> s.price
490.1
>>> help(Stock)
... посмотрите на вывод...
>>>
```

Запустите свои юнит-тесты в `teststock.py` снова. Вы должны увидеть, что по крайней мере один тест пройдет. Ура!

На этом этапе может показаться, что мы сделали огромный шаг назад. Не только классы нуждаются в методе `__init__()`, они также нуждаются в переменной `_fields` для работы некоторых других методов (`__repr__()` и `__setattr__()`). Кроме того, использование `self._init()` выглядит довольно хакерским. Мы поработаем над этим, но будьте терпеливы.
