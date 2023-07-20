# Fixing the Names

One annoying thing about descriptors is the redundant name specification. For example:

```python
class Stock:
    ...
    shares = PositiveInteger('shares')
    ...
```

We can fix that. Change the top-level `Validator` class to include a `__set_name__()` method
like this:

```python
# validate.py

class Validator:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, cls, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)
```

Now, try rewriting your `Stock` class so that it looks like this:

```python
class Stock:
    name   = String()
    shares = PositiveInteger()
    price  = PositiveFloat()

    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
```

Ah, much nicer. Be aware that this ability to set the name is a Python 3.6
feature however. It won't work on older versions.
