# От валидаторов до дескрипторов

В предыдущей задаче вы написали серию классов, которые могут выполнять проверку. Например:

```python
>>> PositiveInteger.check(10)
10
>>> PositiveInteger.check('10')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise TypeError('Expected %s' % cls.expected_type)
TypeError: expected <class 'int'>
>>> PositiveInteger.check(-10)
```

Вы можете расширить это до дескрипторов, выполнив простое изменение в базовом классе `Validator`. Измените его следующим образом:

```python
# validate.py

class Validator:
    def __init__(self, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)
```

Примечание: Отсутствие метода `__get__()` в дескрипторе означает, что Python будет использовать свою стандартную реализацию поиска атрибута. Это требует, чтобы имя, переданное в метод, совпадало с именем, используемым в словаре экземпляра.

Другие изменения не должны потребоваться. Теперь попробуйте изменить класс `Stock`, чтобы использовать валидаторы в качестве дескрипторов, как показано ниже:

```python
class Stock:
    name   = String('name')
    shares = PositiveInteger('shares')
    price  = PositiveFloat('price')

    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
```

Вы увидите, что ваш класс работает так же, как и раньше, при этом в нем на много меньше кода, и он выполняет все нужные проверки:

```python
>>> s = Stock('GOOG', 100, 490.10)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.shares = 75
>>> s.shares = '75'
... TypeError...
>>> s.shares = -50
... ValueError...
>>>
```

Это довольно круто. Дескрипторы позволили вам значительно упростить реализацию класса `Stock`. Именно это и есть настоящая сила дескрипторов - вы получаете низкоуровневый контроль над оператором точки и можете использовать его для выполнения удивительных вещей.
