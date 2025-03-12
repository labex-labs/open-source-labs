# Applying Decorators via Inheritance

In Step 2, we created a class decorator that simplifies our code. However, we still need to explicitly apply the `@validate_attributes` decorator to each class. We can improve this further by applying the decorator automatically through inheritance.

Python's `__init_subclass__` method was introduced in Python 3.6 to allow parent classes to customize the initialization of subclasses. We can use this feature to automatically apply our decorator to any class that inherits from `Structure`.

Let's implement this:

1. Open the `structure.py` file:

```bash
code ~/project/structure.py
```

2. Add the `__init_subclass__` method to the `Structure` class:

```python
class Structure:
    _fields = ()
    _types = ()

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

    def __repr__(self):
        values = ', '.join(repr(getattr(self, name)) for name in self._fields)
        return f'{type(self).__name__}({values})'

    @classmethod
    def create_init(cls):
        '''
        Create an __init__ method from _fields
        '''
        body = 'def __init__(self, %s):\n' % ', '.join(cls._fields)
        for name in cls._fields:
            body += f'    self.{name} = {name}\n'

        # Execute the function creation code
        namespace = {}
        exec(body, namespace)
        setattr(cls, '__init__', namespace['__init__'])

    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)
```

The added `__init_subclass__` method automatically applies the `validate_attributes` decorator to every subclass of `Structure`.

3. Save the file.

4. Now, let's update our `stock.py` file to take advantage of this new feature:

```bash
code ~/project/stock.py
```

5. Modify the `stock.py` file to remove the explicit decorator:

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

Note that we:

- Removed the `validate_attributes` import
- Removed the `@validate_attributes` decorator
- The code now relies solely on inheritance from `Structure`

6. Run the tests again to verify everything still works:

```bash
cd ~/project
python3 teststock.py
```

You should see all tests passing:

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

Let's test our Stock class again to make sure it works as expected:

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

Output:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

This implementation is even cleaner! By using `__init_subclass__`, we've eliminated the need to explicitly apply decorators. Any class that inherits from `Structure` automatically gets the validation behavior.
