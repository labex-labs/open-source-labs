# Applying Decorators via Inheritance

In Step 2, we created a class decorator that simplifies our code. A class decorator is a special type of function that takes a class as an argument and returns a modified class. It's a useful tool in Python for adding functionality to classes without modifying their original code. However, we still need to explicitly apply the `@validate_attributes` decorator to each class. This means that every time we create a new class that needs validation, we have to remember to add this decorator, which can be a bit cumbersome.

We can improve this further by applying the decorator automatically through inheritance. Inheritance is a fundamental concept in object - oriented programming where a subclass can inherit attributes and methods from a parent class. Python's `__init_subclass__` method was introduced in Python 3.6 to allow parent classes to customize the initialization of subclasses. This means that when a subclass is created, the parent class can perform some actions on it. We can use this feature to automatically apply our decorator to any class that inherits from `Structure`.

Let's implement this:

1. Open the `structure.py` file in your editor. This file contains the definition of the `Structure` class, and we are going to modify it to use the `__init_subclass__` method.

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

The `__init_subclass__` method is a class method, which means it can be called on the class itself rather than an instance of the class. When a subclass of `Structure` is created, this method will be automatically called. Inside this method, we call the `validate_attributes` decorator on the subclass `cls`. This way, every subclass of `Structure` will automatically have the validation behavior.

3. Save the file.

After making changes to the `structure.py` file, we need to save it so that the changes are applied.

4. Now, let's update our `stock.py` file to take advantage of this new feature. Open the `stock.py` file in your editor to modify it. This file contains the definition of the `Stock` class, and we are going to make it inherit from the `Structure` class to use the automatic decorator application.

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

- Removed the `validate_attributes` import because we no longer need to import it explicitly since the decorator is applied automatically through inheritance.
- Removed the `@validate_attributes` decorator because the `__init_subclass__` method in the `Structure` class will take care of applying it.
- The code now relies solely on inheritance from `Structure` to get the validation behavior.

6. Run the tests again to verify everything still works:

```bash
cd ~/project
python3 teststock.py
```

Running the tests is important to make sure that our changes haven't broken anything. If all the tests pass, it means that the automatic decorator application through inheritance is working correctly.

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

This command creates an instance of the `Stock` class and prints its representation and the cost. If the output is as expected, it means that the `Stock` class is working correctly with the automatic decorator application.

Output:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

This implementation is even cleaner! By using `__init_subclass__`, we've eliminated the need to explicitly apply decorators. Any class that inherits from `Structure` automatically gets the validation behavior.
