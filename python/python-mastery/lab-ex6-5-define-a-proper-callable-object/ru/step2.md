# Создание вызываемого объекта

В файле `validate.py` начните с создания класса следующим образом:

```python
# validate.py
...

class ValidatedFunction:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Calling', self.func)
        result = self.func(*args, **kwargs)
        return result
```

Протестируйте класс, применяя его к функции:

```python
>>> def add(x, y):
        return x + y

>>> add = ValidatedFunction(add)
>>> add(2, 3)
Calling <function add at 0x1014df598>
5
>>>
```
