# Упражнение 7.7: Использование замыканий для избежания повторений

Одной из более мощных функций замыканий является их использование для генерации повторяющегося кода. Если вы вспомните упражнение 5.7, вспомните код для определения свойства с проверкой типа.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
  ...
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
  ...
```

Вместо того, чтобы многократно повторять этот код, вы можете автоматически создавать его с использованием замыкания.

Создайте файл `typedproperty.py` и поместите в него следующий код:

```python
# typedproperty.py

def typedproperty(name, expected_type):
    private_name = '_' + name
    @property
    def prop(self):
        return getattr(self, private_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, value)

    return prop
```

Теперь, попробуйте его, определив класс следующим образом:

```python
from typedproperty import typedproperty

class Stock:
    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Попробуйте создать экземпляр и проверить, работает ли проверка типа.

```python
>>> s = Stock('IBM', 50, 91.1)
>>> s.name
'IBM'
>>> s.shares = '100'
... должен получиться TypeError...
>>>
```
