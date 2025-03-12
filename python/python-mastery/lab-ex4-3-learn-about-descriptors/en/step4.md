# Improving Descriptor Implementation

In this step, we're going to enhance our descriptor implementation. You might have noticed that in some cases, we've been specifying names redundantly. This can make our code a bit messy and harder to maintain. To solve this problem, we'll use the `__set_name__` method, a useful feature introduced in Python 3.6.

The `__set_name__` method is called automatically when the class is defined. Its main job is to set the name of the descriptor for us, so we don't have to do it manually every time. This will make our code cleaner and more efficient.

Now, let's update your `validate.py` file to include the `__set_name__` method. Here's how the updated code will look:

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

In the code above, the `__set_name__` method in the `Validator` class checks if the `name` attribute is `None`. If it is, it sets the `name` to the actual attribute name used in the class definition. This way, we don't have to specify the name explicitly when creating instances of the descriptor classes.

Now that we've updated the `validate.py` file, we can create an improved version of our `Stock` class. This new version won't require us to specify the names redundantly. Here's the code for the improved `Stock` class:

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

In this `Stock` class, we simply create instances of the `String`, `PositiveInteger`, and `PositiveFloat` descriptor classes without specifying the names. The `__set_name__` method in the `Validator` class will take care of setting the names automatically.

Let's test our improved `Stock` class. First, open your terminal and navigate to the project directory. Then, run the `improved_stock.py` file in interactive mode. Here are the commands to do that:

```bash
cd ~/project
python3 -i improved_stock.py
```

Once you're in the interactive Python session, you can try the following commands to test the functionality of the `Stock` class:

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

These commands create an instance of the `Stock` class, print its attributes, change the value of an attribute, and then try to set invalid values to see if the appropriate errors are raised.

The `__set_name__` method automatically sets the descriptor's name when the class is defined. This makes your code cleaner and less redundant, as you no longer need to specify the attribute name twice.

This improvement demonstrates how Python's descriptor protocol continues to evolve, making it easier to write clean, maintainable code.
