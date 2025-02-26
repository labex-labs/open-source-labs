# Использование классовых декораторов для заполнения деталей

Неприятной особенностью вышеприведенного кода является то, что есть дополнительные детали, такие как переменная `_fields` и последний шаг `Stock.create_init()`. Большую часть этого можно упаковать в класс-декоратор.

В файле `structure.py` создайте класс-декоратор `@validate_attributes`, который examines тело класса на наличие экземпляров валидаторов и заполняет переменную `_fields`. Например:

```python
# structure.py

from validate import Validator

def validate_attributes(cls):
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)
    cls._fields = [val.name for val in validators]
    return cls
```

Этот код основывается на том, что словари классов упорядочены начиная с Python 3.6. Таким образом, он встретит разные дескрипторы `Validator` в том порядке, в котором они перечислены. Используя этот порядок, вы можете затем заполнить переменную `_fields`. Это позволяет вам писать код, подобный следующему:

```python
# stock.py

from structure import Structure, validate_attributes
from validate import String, PositiveInteger, PositiveFloat

@validate_attributes
class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

Stock.create_init()
```

Как только это будет работать, модифицируйте декоратор `@validate_attributes`, чтобы дополнительно выполнять последний шаг, вызывая `Stock.create_init()`. Это сократит класс до следующего вида:

```python
# stock.py

from structure import Structure, validate_attributes
from validate import String, PositiveInteger, PositiveFloat

@validate_attributes
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
