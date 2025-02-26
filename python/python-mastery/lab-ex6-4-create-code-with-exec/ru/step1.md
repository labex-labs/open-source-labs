# Экспериментируем с exec()

Определите фрагмент кода на Python в строке и попробуйте запустить его:

```python
>>> code = '''
for i in range(n):
    print(i, end=' ')
'''
>>> n = 10
>>> exec(code)
0 1 2 3 4 5 6 7 8 9
>>>
```

Это интересное, но выполнение случайных фрагментов кода особо полезным не является. Более интересное использование `exec()` заключается в создании кода, такого как функции, методы или классы. Попробуйте этот пример, в котором мы создаем функцию `__init__()` для класса.

```python
>>> class Stock:
        _fields = ('name','shares', 'price')

>>> argstr = ','.join(Stock._fields)
>>> code = f'def __init__(self, {argstr}):\n'
>>> for name in Stock._fields:
        code += f'    self.{name} = {name}\n'
>>> print(code)
def __init__(self, name,shares,price):
    self.name = name
    self.shares = shares
    self.price = price

>>> locs = { }
>>> exec(code, locs)
>>> Stock.__init__ = locs['__init__']

>>> # Теперь попробуйте класс
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
>>>
```

В этом примере функция `__init__()` создается непосредственно из переменной `_fields`.
Нет никаких странных хаков, связанных с особым методом `_init()` или кадрами стека.
