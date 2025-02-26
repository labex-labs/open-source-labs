# Просмотр дескрипторов

В упражнении 4.3 вы определили несколько дескрипторов, которые позволяли пользователю определять классы с атрибутами с проверкой типа, как показано ниже:

```python
from validate import String, PositiveInteger, PositiveFloat

class Stock:
    name   = String()
    shares = PositiveInteger()
    price  = PositiveFloat()
  ...
```

Измените класс `Stock` так, чтобы он включал приведенные выше дескрипторы и выглядел теперь так (см. упражнение 6.4):

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    _fields = ('name','shares', 'price')
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

Запустите модульные тесты в `teststock.py`. Вы должны увидеть, что значительное количество тестов проходит с добавлением проверки типа. Отлично.
