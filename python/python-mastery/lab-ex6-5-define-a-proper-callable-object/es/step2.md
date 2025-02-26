# Creando un objeto llamable

En el archivo `validate.py`, comienza creando una clase como esta:

```python
# validate.py
...

class ValidatedFunction:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Llamando', self.func)
        result = self.func(*args, **kwargs)
        return result
```

Prueba la clase aplicándola a una función:

```python
>>> def add(x, y):
        return x + y

>>> add = ValidatedFunction(add)
>>> add(2, 3)
Llamando <function add at 0x1014df598>
5
>>>
```
