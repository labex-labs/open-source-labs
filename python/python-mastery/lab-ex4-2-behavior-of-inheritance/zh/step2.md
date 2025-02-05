# 创建一个值检查器

在练习3.4中，你为 `Stock` 类添加了一些属性，用于检查属性的不同类型和值（例如，股票数量必须是正整数）。让我们进一步探讨这个想法。首先创建一个文件 `validate.py` 并定义以下基类：

```python
# validate.py
class Validator:
    @classmethod
    def check(cls, value):
        return value
```

现在，让我们创建一些用于类型检查的类：

```python
class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'预期为 {cls.expected_type}')
        return super().check(value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str
```

以下是如何使用这些类（注意：使用 `@classmethod` 使我们无需创建实例这一额外步骤，因为我们实际上并不需要实例）：

```python
>>> Integer.check(10)
10
>>> Integer.check('10')
Traceback (最近一次调用最后):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 11, in check
    raise TypeError(f'预期为 {cls.expected_type}')
TypeError: 预期为 <class 'int'>
>>> String.check('10')
'10'
>>>
```

你可以在函数中使用这些验证器。例如：

```python
>>> def add(x, y):
        Integer.check(x)
        Integer.check(y)
        return x + y

>>> add(2, 2)
4
>>> add('2', '3')
Traceback (最近一次调用最后):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in add
  File "validate.py", line 11, in check
    raise TypeError(f'预期为 {cls.expected_type}')
TypeError: 预期为 <class 'int'>
>>>
```

现在，创建一些用于不同类型域检查的更多类：

```python
class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('预期 >= 0')
        return super().check(value)

class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('必须非空')
        return super().check(value)
```

这一切将走向何方？让我们开始像玩积木一样通过多重继承将类组合在一起：

```python
class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass
```

本质上，你正在将现有的验证器组合成新的验证器。是不是很疯狂！然而，现在让我们使用它们来验证一些东西：

```python
>>> PositiveInteger.check(10)
10
>>> PositiveInteger.check('10')
Traceback (最近一次调用最后):
  File "<stdin>", line 1, in <module>
    raise TypeError(f'预期为 {cls.expected_type}')
TypeError: 预期为 <class 'int'>
>>> PositiveInteger.check(-10)
Traceback (最近一次调用最后):
  File "<stdin>", line 1, in <module>
    raise ValueError('预期 >= 0')
ValueError: 必须 >= 0


>>> NonEmptyString.check('hello')
'hello'
>>> NonEmptyString.check('')
Traceback (最近一次调用最后):
  File "<stdin>", line 1, in <module>
    raise ValueError('必须非空')
ValueError: 必须非空
>>>
```

此时，你可能已经完全晕头转向了。然而，将不同的代码片段组合在一起的问题在实际程序中确实会出现。协作式多重继承是用于组织此类问题的工具之一。
