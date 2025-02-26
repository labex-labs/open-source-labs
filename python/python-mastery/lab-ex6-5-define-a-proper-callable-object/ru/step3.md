# Применение проверок

Измените класс `ValidatedFunction` так, чтобы он применял проверки значений, прикрепленные с помощью аннотаций функций. Например:

```python
>>> def add(x: Integer, y:Integer):
        return x + y
>>> add = ValidatedFunction(add)
>>> add(2,3)
5
>>> add('two','three')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 67, in __call__
    self.func.__annotations__[name].check(val)
  File "validate.py", line 21, in check
    raise TypeError(f'Expected {cls.expected_type}')
TypeError: expected <class 'int'>
>>>>
```

Совет: Для этого поэкспериментируйте с связыванием сигнатуры. Используйте метод `bind()` объектов `Signature` для связывания аргументов функции с именами аргументов. Затем сравните эту информацию с атрибутом `__annotations__`, чтобы получить разные классы валидаторов.

Обратите внимание, вы создаете объект, который выглядит как функция, но на самом деле это не так. Там происходит магия под капотом.
