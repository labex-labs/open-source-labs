# Ограничение имен атрибутов

Дайте классу `Structure` метод `__setattr__()`, который ограничивает допустимый набор атрибутов только теми, которые перечислены в переменной `_fields`. Однако, он по-прежнему должен позволять задавать любые "частные" атрибуты (например, имена, начинающиеся с `_`).

Например:

```python
>>> s = Stock('GOOG',100,490.1)
>>> s.shares = 50
>>> s.share = 50
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "structure.py", line 13, in __setattr__
    raise AttributeError('No attribute %s' % name)
AttributeError: No attribute share
>>> s._shares = 100     # Private attribute. OK
>>>
```
