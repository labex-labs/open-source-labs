# Создание класса

Помните, из предыдущих упражнений мы определили простой класс `Stock`, который выглядел так:

```python
class Stock:
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares*self.price
    def sell(self,nshares):
        self.shares -= nshares
```

Теперь мы создадим этот класс вручную. Сначала определим методы как обычные функции на Python.

```python
>>> def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price

>>> def cost(self):
        return self.shares*self.price

>>> def sell(self,nshares):
        self.shares -= nshares

>>>
```

Далее, создадим словарь методов:

```python
>>> methods = {
         '__init__' : __init__,
         'cost' : cost,
         'sell' : sell }

>>>
```

Наконец, создадим объект класса `Stock`:

```python
>>> Stock = type('Stock',(object,),methods)
>>> s = Stock('GOOG',100,490.10)
>>> s.name
'GOOG'
>>> s.cost()
49010.0
>>> s.sell(25)
>>> s.shares
75
>>>
```

Поздравляем, вы только что создали класс. Класс на самом деле представляет собой имя, кортеж базовых классов и словарь, содержащий все содержимое класса. `type()` - это конструктор, который создает класс для вас, если вы передадите эти три части.
