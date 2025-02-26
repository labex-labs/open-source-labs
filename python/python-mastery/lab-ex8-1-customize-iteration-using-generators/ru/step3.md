# Неожиданная сила итерации

Python использует итерацию способами, которые вы, возможно, не ожидаете. После добавления `__iter__()` в класс `Structure` вы обнаружите, что легко выполнять все виды новых операций. Например, преобразования в последовательности и распаковка:

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> list(s)
['GOOG', 100, 490.1]
>>> tuple(s)
('GOOG', 100, 490.1)
>>> name, shares, price = s
>>> name
'GOOG'
>>> shares
100
>>> price
490.1
>>>
```

Пока мы это делаем, мы можем теперь добавить оператор сравнения в наш класс `Structure`:

```python
# structure.py
class Structure(metaclass=StructureMeta):
 ...
    def __eq__(self, other):
        return isinstance(other, type(self)) and tuple(self) == tuple(other)
 ...
```

Теперь вы должны быть able сравнивать объекты:

```python
>>> a = Stock('GOOG', 100, 490.1)
>>> b = Stock('GOOG', 100, 490.1)
>>> a == b
True
>>>
```

Попробуйте снова запустить свои юнит-тесты `teststock.py`. Теперь все должно пройти. Отлично.
