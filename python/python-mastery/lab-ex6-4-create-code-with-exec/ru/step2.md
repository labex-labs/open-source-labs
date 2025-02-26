# Создание функции `__init__()`

В упражнении 6.3 вы писали код, который проверял сигнатуру метода `__init__()`, чтобы установить имена атрибутов в переменную класса `_fields`. Например:

```python
class Stock(Structure):
    def __init__(self, name, shares, price):
        self._init()

Stock.set_fields()
```

Вместо проверки метода `__init__()`, напишите класс-метод `create_init(cls)`, который создает метод `__init__()` из значения `_fields`. Используйте функцию `exec()`, чтобы сделать это, как показано выше. Вот, как пользователь будет использовать его:

```python
class Stock(Structure):
    _fields = ('name','shares', 'price')

Stock.create_init()
```

Результирующий класс должен работать точно так же, как и раньше:

```python
>>> s = Stock(name='GOOG', shares=100, price=490.1)
>>> s
Stock('GOOG',100,490.1)
>>> s.shares = 50
>>> s.share = 50
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "structure.py", line 12, in __setattr__
    raise AttributeError('No attribute %s' % name)
AttributeError: No attribute share
>>>
```

Измените класс `Stock` в процессе, чтобы использовать функцию `create_init()`, как показано.
Проверьте с помощью своих юнит-тестов, как и раньше.

Пока вы это делаете, удалите методы `_init()` и `set_fields()` из класса `Structure` - этот подход был довольно странным.
