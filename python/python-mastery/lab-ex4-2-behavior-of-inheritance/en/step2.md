# Building a Validation System with Inheritance

In this step, we'll build a practical validation system using inheritance. This will demonstrate how inheritance can be used to create reusable code components that can be composed in different ways.

## Creating the Base Validator Class

First, let's create a new file called `validate.py` in the WebIDE. Click on "File" > "New File" or use the keyboard shortcut, then name it `validate.py`.

Add the following code to create a base `Validator` class:

```python
# validate.py
class Validator:
    @classmethod
    def check(cls, value):
        return value
```

This simple base class defines a `check` method that takes a value and returns it unchanged. The `@classmethod` decorator means we can call this method on the class itself, without creating an instance.

## Adding Type Validators

Now let's add some validators that check the type of a value. Add the following code to `validate.py`:

```python
class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str
```

The `Typed` class checks if a value is of the expected type, raising a `TypeError` if not. The `Integer`, `Float`, and `String` classes inherit from `Typed` and specify the exact type to check for.

## Testing the Type Validators

Let's test our validators. Open a new terminal and start the Python interpreter:

```bash
python3
```

Now import and test our validators:

```python
from validate import Integer, String

Integer.check(10)  # Should return 10

try:
    Integer.check('10')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

String.check('10')  # Should return '10'
```

You should see something like:

```
10
Error: Expected <class 'int'>
'10'
```

We could use these validators in a function. Try this:

```python
def add(x, y):
    Integer.check(x)
    Integer.check(y)
    return x + y

add(2, 2)  # Should return 4

try:
    add('2', '3')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")
```

You should see:

```
4
Error: Expected <class 'int'>
```

## Adding Value Validators

Now let's add validators that check the value rather than the type. Go back to `validate.py` and add:

```python
class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        return super().check(value)

class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty')
        return super().check(value)
```

The `Positive` validator checks if a value is non-negative, and the `NonEmpty` validator checks if a value has a non-zero length.

## Composing Validators with Multiple Inheritance

Now let's combine our validators using multiple inheritance. Add the following code to `validate.py`:

```python
class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass
```

These new classes combine type checking and value checking. For example, `PositiveInteger` checks that a value is both an integer and non-negative.

## Testing the Composed Validators

Let's test our composed validators. In the Python interpreter:

```python
from validate import PositiveInteger, PositiveFloat, NonEmptyString

PositiveInteger.check(10)  # Should return 10

try:
    PositiveInteger.check('10')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

try:
    PositiveInteger.check(-10)  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")

NonEmptyString.check('hello')  # Should return 'hello'

try:
    NonEmptyString.check('')  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")
```

You should see:

```
10
Error: Expected <class 'int'>
Error: Expected >= 0
'hello'
Error: Must be non-empty
```

This demonstrates how we can compose validators to create more complex validation rules. The order of inheritance matters here - the validators are checked in the order specified in the class definition.

You can exit the Python interpreter when you're done:

```python
exit()
```
