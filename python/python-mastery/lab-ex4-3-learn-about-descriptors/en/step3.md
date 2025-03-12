# Implementing Validators Using Descriptors

In this step, we're going to create a validation system using descriptors. But first, let's understand what descriptors are and why we're using them. Descriptors are Python objects that implement the descriptor protocol, which includes the `__get__`, `__set__`, or `__delete__` methods. They allow you to customize how an attribute is accessed, set, or deleted on an object. In our case, we'll use descriptors to create a validation system that ensures data integrity. This means that the data stored in our objects will always meet certain criteria, like being of a specific type or having a positive value.

Now, let's start creating our validation system. We'll create a new file called `validate.py` in the project directory. This file will contain the classes that implement our validators.

```python
# validate.py

class Validator:
    def __init__(self, name):
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

In the `validate.py` file, we first define a base class called `Validator`. This class has an `__init__` method that takes a `name` parameter, which will be used to identify the attribute being validated. The `check` method is a class method that simply returns the value passed to it. The `__set__` method is a descriptor method that is called when an attribute is set on an object. It calls the `check` method to validate the value and then stores the validated value in the object's dictionary.

We then define three subclasses of `Validator`: `String`, `PositiveInteger`, and `PositiveFloat`. Each of these subclasses overrides the `check` method to perform specific validation checks. The `String` class checks if the value is a string, the `PositiveInteger` class checks if the value is a positive integer, and the `PositiveFloat` class checks if the value is a positive number (either an integer or a float).

Now that we have our validators defined, let's modify our `Stock` class to use these validators. We'll create a new file called `stock_with_validators.py` and import the validators from the `validate.py` file.

```python
# stock_with_validators.py

from validate import String, PositiveInteger, PositiveFloat

class Stock:
    name = String('name')
    shares = PositiveInteger('shares')
    price = PositiveFloat('price')

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

In the `stock_with_validators.py` file, we define the `Stock` class and use the validators as class attributes. This means that whenever an attribute is set on a `Stock` object, the corresponding validator's `__set__` method will be called to validate the value. The `__init__` method initializes the attributes of the `Stock` object, and the `cost`, `sell`, and `__repr__` methods provide additional functionality.

Now, let's test our validator-based `Stock` class. We'll open a terminal, navigate to the project directory, and run the `stock_with_validators.py` file in interactive mode.

```bash
cd ~/project
python3 -i stock_with_validators.py
```

Once the Python interpreter is running, we can try some commands to test the validation system.

```python
# Create a stock with valid values
s = Stock('GOOG', 100, 490.10)
print(s.name)    # Should return 'GOOG'
print(s.shares)  # Should return 100
print(s.price)   # Should return 490.1

# Try changing to valid values
s.shares = 75
print(s.shares)  # Should return 75

# Try setting invalid values
try:
    s.shares = '75'  # Should raise TypeError
except TypeError as e:
    print(f"Error setting shares to string: {e}")

try:
    s.shares = -50  # Should raise ValueError
except ValueError as e:
    print(f"Error setting negative shares: {e}")

exit()
```

In the test code, we first create a `Stock` object with valid values and print its attributes to verify that they are set correctly. We then try to change the `shares` attribute to a valid value and print it again to confirm the change. Finally, we try to set the `shares` attribute to an invalid value (a string and a negative number) and catch the exceptions that are raised by the validators.

Notice how our code is now much cleaner. The `Stock` class no longer needs to implement all those property methods - the validators handle all the type checking and constraints.

Descriptors have allowed us to create a reusable validation system that can be applied to any class attribute. This is a powerful pattern for maintaining data integrity across your application.
