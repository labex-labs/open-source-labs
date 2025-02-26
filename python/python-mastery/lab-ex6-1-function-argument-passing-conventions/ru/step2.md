# Упрощенные структуры данных

В предыдущих упражнениях вы определяли класс, представляющий акцию, следующим образом:

```python
class Stock:
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
```

Обратите внимание на метод `__init__()` - это не слишком много кода для набора каждый раз, когда вы хотите заполнить структуру? Что, если вам пришлось бы определить десятки таких структур в вашей программе?

В файле `structure.py` определите базовый класс `Structure`, который позволяет пользователю определять простые структуры данных, как показано ниже:

```python
class Stock(Structure):
    _fields = ('name','shares','price')

class Date(Structure):
    _fields = ('year','month', 'day')
```

Класс `Structure` должен определить метод `__init__()`, который принимает любое количество аргументов и ищет наличие переменной класса `_fields`. Дайте методу заполнить экземпляр из имен атрибутов в `_fields` и значений, переданных в `__init__()`.

Вот пример кода для проверки вашей реализации:

```python
>>> s = Stock('GOOG',100,490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
>>> s = Stock('AA',50)
Traceback (most recent call last):
...
TypeError: Expected 3 arguments
>>>
```
