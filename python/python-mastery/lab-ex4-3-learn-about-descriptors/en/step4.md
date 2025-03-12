# Improving Descriptor Implementation

In this step, we'll improve our descriptor implementation by removing redundant name specifications. This is done using the `__set_name__` method, a feature introduced in Python 3.6.

Update your `validate.py` file to include the `__set_name__` method:

```python
# validate.py

class Validator:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, cls, name):
        # This gets called when the class is defined
        # It automatically sets the name of the descriptor
        if self.name is None:
            self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)


class String(Validator):
    expected_type = str

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return value


class PositiveInteger(Validator):
    expected_type = int

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        if value < 0:
            raise ValueError('Expected a positive value')
        return value


class PositiveFloat(Validator):
    expected_type = float

    @classmethod
    def check(cls, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Expected a number')
        if value < 0:
            raise ValueError('Expected a positive value')
        return float(value)
```

Now we can create an improved version of our `Stock` class that doesn't require redundant name specifications:

```python
# improved_stock.py

from validate import String, PositiveInteger, PositiveFloat

class Stock:
    name = String()  # No need to specify 'name' anymore
    shares = PositiveInteger()
    price = PositiveFloat()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        self.shares -= amount

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
```

Let's test our improved Stock class:

```bash
cd ~/project
python3 -i improved_stock.py
```

Try these commands:

```python
s = Stock('GOOG', 100, 490.10)
print(s.name)    # Should return 'GOOG'
print(s.shares)  # Should return 100
print(s.price)   # Should return 490.1

# Try changing values
s.shares = 75
print(s.shares)  # Should return 75

# Try invalid values
try:
    s.shares = '75'  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

try:
    s.price = -10.5  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")

exit()
```

The `__set_name__` method automatically sets the descriptor's name when the class is defined. This makes your code cleaner and less redundant, as you no longer need to specify the attribute name twice.

This improvement demonstrates how Python's descriptor protocol continues to evolve, making it easier to write clean, maintainable code.
