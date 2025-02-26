# Подготовка

В упражнении 4.3 вы создали серию классов `Validator` для выполнения различных видов проверок типов и значений. Например:

```python
>>> from validate import Integer
>>> Integer.check(1)
>>> Integer.check('hello')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 21, in check
    raise TypeError(f'Expected {cls.expected_type}')
TypeError: Expected <class 'int'>
>>>
```

Вы могли использовать валидаторы в функциях так:

```python
>>> def add(x, y):
        Integer.check(x)
        Integer.check(y)
        return x + y

>>>
```

В этом упражнении мы пойдем немного дальше.
