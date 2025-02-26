# Создайте проверщик значений

В упражнении 3.4 вы добавили некоторые свойства в класс `Stock`, которые проверяли атрибуты на разные типы и значения (например, количество акций должно быть положительным целым числом). Давайте немного поиграем с этой идеей. Начните с создания файла `validate.py` и определения следующего базового класса:

```python
# validate.py
class Validator:
    @classmethod
    def check(cls, value):
        return value
```

Теперь давайте создадим несколько классов для проверки типов:

```python
class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str
```

Вот, как вы можете использовать эти классы (Примечание: использование `@classmethod` позволяет избежать лишнего шага по созданию экземпляров, которых мы на самом деле не нуждаемся):

```python
>>> Integer.check(10)
10
>>> Integer.check('10')
Traceback (most recent call last):
  File "<stdin>", line 1, in check
    raise TypeError(f'Expected {cls.expected_type}')
TypeError: Expected <class 'int'>
>>> String.check('10')
'10'
>>>
```

Вы можете использовать проверяющие функции в другой функции. Например:

```python
>>> def add(x, y):
        Integer.check(x)
        Integer.check(y)
        return x + y

>>> add(2, 2)
4
>>> add('2', '3')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in add
  File "validate.py", line 11, in check
    raise TypeError(f'Expected {cls.expected_type}')
TypeError: Expected <class 'int'>
>>>
```

Теперь создайте несколько более классов для различных видов проверки домена:

```python
class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        return super().check(value)

class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty')
        return super().check(value)
```

Куда это все приведет? Давайте начнем комбинировать классы вместе с помощью множественного наследования, как если бы они были детскими积木ками:

```python
class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass
```

По сути, вы берете существующих проверяющих классов и комбинируете их в новые. Безумство! Однако, давайте теперь используем их для проверки некоторых вещей:

```python
>>> PositiveInteger.check(10)
10
>>> PositiveInteger.check('10')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise TypeError(f'Expected {cls.expected_type}')
TypeError: Expected <class 'int'>
>>> PositiveInteger.check(-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise ValueError('Expected >= 0')
ValueError: Must be >= 0


>>> NonEmptyString.check('hello')
'hello'
>>> NonEmptyString.check('')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise ValueError('Must be non-empty')
ValueError: Must be non-empty
>>>
```

На этом этапе ваш мозг, вероятно, уже полностью взорвался. Однако проблема комбинирования различных частей кода возникает в реальных программах. Совместное множественное наследование - это один из инструментов, который можно использовать для ее организации.
