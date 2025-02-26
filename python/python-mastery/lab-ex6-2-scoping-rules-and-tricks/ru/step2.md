# Покажите мне ваши локальные переменные

Сначала попробуйте провести эксперимент, определив следующий класс:

```python
>>> class Stock:
        def __init__(self, name, shares, price):
            print(locals())

>>>
```

Теперь попробуйте запустить это:

```python
>>> s = Stock('GOOG', 100, 490.1)
{'self': <__main__.Stock object at 0x100699b00>, 'price': 490.1, 'name': 'GOOG','shares': 100}
>>>
```

Заметьте, как словарь локальных переменных содержит все аргументы, переданные в `__init__()`. Это интересно. Теперь определите следующие функции и определения класса:

```python
>>> def _init(locs):
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)

>>> class Stock:
        def __init__(self, name, shares, price):
            _init(locals())
```

В этом коде функция `_init()` используется для автоматической инициализации объекта из словаря переданных локальных переменных. Вы обнаружите, что `help(Stock)` и аргументы по ключевым словам работают идеально.

```python
>>> s = Stock(name='GOOG', price=490.1, shares=50)
>>> s.name
'GOOG'
>>> s.shares
50
>>> s.price
490.1
>>>
```
