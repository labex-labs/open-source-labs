# Creating a Callable Object

In the file `validate.py`, start by creating a class like this:

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

Test the class by applying it to a function:

```python
>>> def add(x, y):
        return x + y

>>> add = ValidatedFunction(add)
>>> add(2, 3)
Calling <function add at 0x1014df598>
5
>>>
```
