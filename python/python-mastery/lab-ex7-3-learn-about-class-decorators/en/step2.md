# Creating a Class Decorator for Validation

While our implementation from Step 1 works, there's redundancy in having to specify both the `_fields` tuple and the descriptor attributes. We can improve this by creating a class decorator that automatically extracts field information from the descriptors.

Class decorators are functions that take a class as an argument, modify it, and return the modified class. Let's create one to simplify our code:

1. Open the `structure.py` file:

```bash
code ~/project/structure.py
```

2. Add the following code at the top of the file (after any imports):

```python
from validate import Validator

def validate_attributes(cls):
    """
    Class decorator that extracts Validator instances
    and builds the _fields list automatically
    """
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # Set _fields based on validator names
    cls._fields = [val.name for val in validators]

    # Create initialization method
    cls.create_init()

    return cls
```

This decorator:

- Finds all `Validator` instances in the class
- Automatically builds the `_fields` list from their names
- Calls `create_init()` to generate the `__init__` method
- Returns the modified class

3. Save the file.

4. Now, let's modify our `stock.py` file to use this decorator:

```bash
code ~/project/stock.py
```

5. Update the `stock.py` file to use the decorator:

```python
# stock.py

from structure import Structure, validate_attributes
from validate import String, PositiveInteger, PositiveFloat

@validate_attributes
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

Notice how we've:

- Added the `@validate_attributes` decorator to the `Stock` class
- Removed the explicit `_fields` declaration
- Removed the call to `Stock.create_init()`

The class is now simpler and cleaner, as the decorator handles these details automatically.

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

Let's test our Stock class interactively:

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

Output:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

Great! You've successfully implemented a class decorator that simplifies our code by automatically handling field declarations and initialization.
