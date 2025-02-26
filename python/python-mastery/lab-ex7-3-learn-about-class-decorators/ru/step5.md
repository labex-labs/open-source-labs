# Проверка аргументов методов

Помните декоратор `@validated`, который вы писали в предыдущей части? Давайте модифицируем декоратор `@validate_attributes`, чтобы любой метод в классе с аннотациями автоматически оборачивался декоратором `@validated`. Это позволяет ставить обязательные аннотации на методы, такие как метод `sell()`:

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

Вы увидите, что метод `sell()` теперь проверяет аргумент.

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.sell(25)
>>> s.sell(-25)
Traceback (most recent call last):
...
TypeError: Bad Arguments
  nshares: must be >= 0
>>>
```

Да, это теперь становится очень интересным. Комбинация класса-декоратора и наследования является мощной силой.
