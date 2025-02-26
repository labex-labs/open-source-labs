# Замыкания в качестве генератора кода

В упражнении 4.3 вы разработали набор классов-дескрипторов, которые позволяли проводить проверку типов атрибутов объектов. Например:

```python

class Stock:
    name = String()
    shares = Integer()
    price = Float()
```

Такой подход также можно реализовать с использованием замыканий. Определите файл `typedproperty.py` и поместите в него следующий код:

```python
# typedproperty.py

def typedproperty(name, expected_type):
    private_name = '_' + name

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, val)

    return value
```

Это выглядит довольно странно, но функция фактически генерирует код. Вы бы использовали ее в определении класса так:

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

Проверьте, что этот класс проводит проверку типов точно так же, как и код с использованием дескрипторов.

Добавьте функции `String()`, `Integer()` и `Float()` в файл `typedproperty.py`, чтобы можно было написать следующий код:

```python
from typedproperty import String, Integer, Float

class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```
