# Применение правил проверки

С использованием свойств и приватных атрибутов измените атрибут `shares` класса `Stock` так, чтобы он мог быть присвоен только неотрицательному целочисленному значению. Кроме того, измените атрибут `price` так, чтобы он мог быть присвоен только неотрицательному значению с плавающей точкой.

Новый объект должен работать практически так же, как и старый, за исключением дополнительной проверки типа и значения.

```python
>>> s = Stock('GOOG', 100, 490.10)
>>> s.shares = 50          # OK
>>> s.shares = '50'
Traceback (most recent call last):
...
TypeError: Expected integer
>>> s.shares = -10
Traceback (most recent call last):
...
ValueError: shares must be >= 0

>>> s.price = 123.45       # OK
>>> s.price = '123.45'
Traceback (most recent call last):
...
TypeError: Expected float
>>> s.price = -10.0
Traceback (most recent call last):
...
ValueError: price must be >= 0
>>>
```
