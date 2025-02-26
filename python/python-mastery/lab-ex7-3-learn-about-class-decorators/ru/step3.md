# Применение декораторов с использованием наследования

Некогда нужно указывать сам класс-декоратор, что довольно неудобно. Измените класс `Structure` с использованием следующего метода `__init_subclass__()`:

```python
# structure.py

class Structure:
 ...
    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)
```

После внесения этого изменения вы должны быть в состоянии полностью отказаться от декоратора и полностью полагаться только на наследование. Это наследование плюс некоторую скрытую магию!

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

    def sell(self, nshares):
        self.shares -= nshares
```

Теперь код действительно начинает становиться более простым. Фактически, он почти выглядит обычным. Давайте продолжим улучшать его.
