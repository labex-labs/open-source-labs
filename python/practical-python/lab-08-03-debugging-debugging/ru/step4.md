# Дебаггинг с использованием print

Дебаггинг с использованием `print()` - это довольно распространенный метод.

_Совет: убедитесь, что используете `repr()`_

```python
def spam(x):
    print('DEBUG:', repr(x))
  ...
```

`repr()` показывает точное представление значения. Не красивый вывод для печати.

```python
>>> from decimal import Decimal
>>> x = Decimal('3.4')
# БЕЗ `repr`
>>> print(x)
3.4
# С `repr`
>>> print(repr(x))
Decimal('3.4')
>>>
```
