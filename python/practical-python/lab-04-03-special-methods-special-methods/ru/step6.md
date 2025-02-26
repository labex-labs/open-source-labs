# Связанные методы

Метод, который еще не был вызван оператором вызова функции `()`, называется _связанным методом_. Он действует на экземпляр, откуда он произошел.

```python
>>> s = stock.Stock('GOOG', 100, 490.10)
>>> s
<Stock object at 0x590d0>
>>> c = s.cost
>>> c
<bound method Stock.cost of <Stock object at 0x590d0>>
>>> c()
49010.0
>>>
```

Связанные методы часто являются источником невнимательных и неочевидных ошибок. Например:

```python
>>> s = stock.Stock('GOOG', 100, 490.10)
>>> print('Cost : %0.2f' % s.cost)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: float argument required
>>>
```

Или скрытого поведения, которое трудно отлаживать.

```python
f = open(filename, 'w')
...
f.close     # Упс, ничего не сделал. `f` по-прежнему открыт.
```

В обоих случаях ошибка возникает из-за забывания поставить конечные круглые скобки. Например, `s.cost()` или `f.close()`.
