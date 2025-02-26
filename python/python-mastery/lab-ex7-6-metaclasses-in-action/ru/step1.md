# Последняя fronteira

В упражнении 7.3 мы сделали возможным определение типизированных структур следующим образом:

```python
from validate import String, PositiveInteger, PositiveFloat
from structure import Structure

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

Под капотом происходит много вещей. Однако, одна досада связана с всеми этими импортами имен типов в начале (например, `String`, `PositiveInteger` и т.д.). Именно такое может привести к инструкции `from validate import *`. Одна интересная вещь о метаклассе заключается в том, что он может быть использован для управления процессом, при котором класс определяется. Это включает в себя управление окружением определения класса сам по себе. Давайте поработаем с этими импортами.

Первым шагом в управлении всеми именами валидаторов является их сбор. Перейдите в файл `validate.py` и модифицируйте базовый класс `Validator` с помощью этого дополнительного куска кода, снова связанного с `__init_subclass__()`:

```python
# validate.py

class Validator:
 ...

    # Собираем все производные классы в словарь
    validators = { }
    @classmethod
    def __init_subclass__(cls):
        cls.validators[cls.__name__] = cls
```

Это не так много, но оно создает небольшое пространство имен всех подклассов `Validator`. Посмотрите на это:

```python
>>> from validate import Validator
>>> Validator.validators
{'Float': <class 'validate.Float'>,
 'Integer': <class 'validate.Integer'>,
 'NonEmpty': <class 'validate.NonEmpty'>,
 'NonEmptyString': <class 'validate.NonEmptyString'>,
 'Positive': <class 'validate.Positive'>,
 'PositiveFloat': <class 'validate.PositiveFloat'>,
 'PositiveInteger': <class 'validate.PositiveInteger'>,
 'String': <class 'validate.String'>,
 'Typed': <class 'validate.Typed'>}
>>>
```

Теперь, когда вы это сделали, давайте внедрим это пространство имен в пространство имен классов, определяемых из `Structure`. Определите следующий метакласс:

```python
# structure.py
...

from validate import Validator
from collections import ChainMap

class StructureMeta(type):
    @classmethod
    def __prepare__(meta, clsname, bases):
        return ChainMap({}, Validator.validators)

    @staticmethod
    def __new__(meta, name, bases, methods):
        methods = methods.maps[0]
        return super().__new__(meta, name, bases, methods)

class Structure(metaclass=StructureMeta):
 ...
```

В этом коде метод `__prepare__()` создает специальную `ChainMap`-отображение, которое состоит из пустого словаря и словаря всех определенных валидаторов. Пустой словарь, перечисленный первым, собирает все определения, сделанные внутри тела класса. Словарь `Validator.validators` делает все определения типов доступными для использования в качестве дескрипторов или аннотаций типов аргументов.

Метод `__new__()` выбрасывает лишний словарь валидатора и передает оставшиеся определения конструктору типа. Это изобретательное решение, но оно позволяет избавиться от раздражающих импортов:

```python
# stock.py

from structure import Structure

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
