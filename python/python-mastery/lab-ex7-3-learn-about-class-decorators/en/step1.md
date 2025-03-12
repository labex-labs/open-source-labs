# Implementing Type-Checking with Descriptors

In this step, you will create a `Stock` class that uses descriptors for type checking. Descriptors are a powerful Python feature that allows you to control attribute access in classes.

Let's start by understanding what descriptors are:

- **Descriptors** are objects that define how attributes are accessed on other objects
- They implement special methods like `__get__`, `__set__`, and `__delete__`
- They're useful for implementing validation, type checking, and computed properties

The `validate.py` file already contains validator classes (`String`, `PositiveInteger`, `PositiveFloat`) that we can use for attribute validation.

Let's create our `Stock` class with descriptors:

1. Open the `stock.py` file in the editor:

```bash
code ~/project/stock.py
```

2. Replace the placeholder content with the following code:

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    _fields = ('name', 'shares', 'price')
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

# Create an __init__ method based on _fields
Stock.create_init()
```

Let's understand what's happening in this code:

- The `_fields` tuple defines the attributes of the `Stock` class
- `name`, `shares`, and `price` are defined as descriptor objects that validate their values
- The `cost` property calculates the total cost based on shares and price
- The `sell` method reduces the number of shares
- `Stock.create_init()` dynamically creates an `__init__` method for our class

3. Save the file.

4. Run the tests to verify your implementation:

```bash
cd ~/project
python3 teststock.py
```

You should see output similar to this:

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

This means all the tests are passing. The descriptors are successfully validating the types of each attribute!

Try creating a `Stock` object in the Python interpreter:

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); print(s); print(f'Cost: {s.cost}')"
```

Output:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

You've successfully implemented descriptors for type-checking! Now, let's improve this code further.
