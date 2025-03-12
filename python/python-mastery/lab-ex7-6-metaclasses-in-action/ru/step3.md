# Создание метакласса StructureMeta

Теперь давайте поговорим о том, что мы будем делать дальше. Мы нашли способ собрать все типы валидаторов. Нашим следующим шагом является создание метакласса. Но что же такое метакласс? В Python метакласс - это особый тип класса. Его экземпляры сами являются классами. Это означает, что метакласс может контролировать, как класс создается. Он может управлять пространством имен, где определяются атрибуты класса.

В нашей ситуации мы хотим создать метакласс, который сделает типы валидаторов доступными при определении подкласса `Structure`. Мы не хотим каждый раз явно импортировать эти типы валидаторов.

Давайте начнем с того, что откроем снова файл `structure.py`. Вы можете использовать следующую команду для его открытия:

```bash
code structure.py
```

После того, как файл открыт, нам нужно добавить некоторый код в начале, перед определением класса `Structure`. Этот код определит наш метакласс.

```python
from validate import Validator
from collections import ChainMap

class StructureMeta(type):
    @classmethod
    def __prepare__(meta, clsname, bases):
        """Prepare the namespace for the class being defined"""
        return ChainMap({}, Validator.validators)

    @staticmethod
    def __new__(meta, name, bases, methods):
        """Create the new class using only the local namespace"""
        methods = methods.maps[0]  # Extract the local namespace
        return super().__new__(meta, name, bases, methods)
```

Теперь, когда мы определили метакласс, нам нужно модифицировать класс `Structure`, чтобы использовать его. Таким образом, любой класс, который наследуется от `Structure`, будет использовать функциональность метакласса.

```python
class Structure(metaclass=StructureMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')

        # Set all of the positional arguments
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

        # Set the remaining keyword arguments
        for name, val in kwargs.items():
            if name not in self._fields:
                raise TypeError(f'Invalid argument: {name}')
            setattr(self, name, val)

    def __repr__(self):
        values = [getattr(self, name) for name in self._fields]
        args_str = ','.join(repr(val) for val in values)
        return f'{type(self).__name__}({args_str})'
```

Давайте разберем, что делает этот код:

1. Метод `__prepare__()` - это специальный метод в Python. Он вызывается перед созданием класса. Его задача - подготовить пространство имен, где будут определены атрибуты класса. Здесь мы используем `ChainMap`. `ChainMap` - это полезный инструмент, который создает слоистый словарь. В нашем случае он включает наши типы валидаторов, делая их доступными в пространстве имен класса.

2. Метод `__new__()` отвечает за создание нового класса. Мы извлекаем только локальное пространство имен, которое является первым словарем в `ChainMap`. Мы отбрасываем словарь валидаторов, потому что мы уже сделали типы валидаторов доступными в пространстве имен.

При такой настройке любой класс, который наследуется от `Structure`, будет иметь доступ ко всем типам валидаторов без необходимости явного импорта.

Теперь давайте протестируем нашу реализацию. Мы создадим класс `Stock`, используя наш расширенный базовый класс `Structure`.

```bash
cat > stock.py << EOF
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
EOF
```

Если наш метакласс работает правильно, мы должны быть able to определить класс `Stock` без импорта типов валидаторов. Это потому, что метакласс уже сделал их доступными в пространстве имен.
