# Исправление имен

Одна из неудобных вещей при работе с дескрипторами - это избыточное указание имени. Например:

```python
class Stock:
  ...
    shares = PositiveInteger('shares')
  ...
```

Мы можем это исправить. Измените верхнеуровневый класс `Validator` так, чтобы он включал метод `__set_name__()`, как показано ниже:

```python
# validate.py

class Validator:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, cls, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)
```

Теперь попробуйте переписать класс `Stock` так, чтобы он выглядел следующим образом:

```python
class Stock:
    name   = String()
    shares = PositiveInteger()
    price  = PositiveFloat()

    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
```

Ах, куда приятнее. Обратите внимание, что эта возможность задавать имя - это особенность Python 3.6. Она не будет работать в более старых версиях.
