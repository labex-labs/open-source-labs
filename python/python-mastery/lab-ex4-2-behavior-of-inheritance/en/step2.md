# Building a Validation System with Inheritance

In this step, we're going to build a practical validation system using inheritance. Inheritance is a powerful concept in programming that allows you to create new classes based on existing ones. This way, you can reuse code and create more organized and modular programs. By building this validation system, you'll see how inheritance can be used to create reusable code components that can be combined in different ways.

## Creating the Base Validator Class

First, we need to create a base class for our validators. To do this, we'll create a new file in the WebIDE. Here's how you can do it: click on "File" > "New File", or you can use the keyboard shortcut. Once the new file is open, name it `validate.py`.

Now, let's add some code to this file to create a base `Validator` class. This class will serve as the foundation for all our other validators.

```python
# validate.py
class Validator:
    @classmethod
    def check(cls, value):
        return value
```

In this code, we've defined a `Validator` class with a `check` method. The `check` method takes a value as an argument and simply returns it unchanged. The `@classmethod` decorator is used to make this method a class method. This means we can call this method on the class itself, without having to create an instance of the class.

## Adding Type Validators

Next, we'll add some validators that check the type of a value. These validators will inherit from the `Validator` class we just created. Go back to the `validate.py` file and add the following code:

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

The `Typed` class is a subclass of `Validator`. It has an `expected_type` attribute, which is initially set to `object`. The `check` method in the `Typed` class checks if the given value is of the expected type. If it's not, it raises a `TypeError`. If the type is correct, it calls the `check` method of the parent class using `super().check(value)`.

The `Integer`, `Float`, and `String` classes inherit from `Typed` and specify the exact type they are supposed to check for. For example, the `Integer` class checks if a value is an integer.

## Testing the Type Validators

Now that we've created our type validators, let's test them. Open a new terminal and start the Python interpreter by running the following command:

```bash
python3
```

Once the Python interpreter is running, we can import and test our validators. Here's some code to test them:

```python
from validate import Integer, String

Integer.check(10)  # Should return 10

try:
    Integer.check('10')  # Should raise TypeError
except TypeError as e:
    print(f"Error: {e}")

String.check('10')  # Should return '10'
```

When you run this code, you should see something like this:

```
10
Error: Expected <class 'int'>
'10'
```

We can also use these validators in a function. Let's try that:

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

When you run this code, you should see:

```
4
Error: Expected <class 'int'>
```

## Adding Value Validators

So far, we've created validators that check the type of a value. Now, let's add some validators that check the value itself rather than the type. Go back to the `validate.py` file and add the following code:

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

The `Positive` validator checks if a value is non-negative. If the value is less than 0, it raises a `ValueError`. The `NonEmpty` validator checks if a value has a non-zero length. If the length is 0, it raises a `ValueError`.

## Composing Validators with Multiple Inheritance

Now, we're going to combine our validators using multiple inheritance. Multiple inheritance allows a class to inherit from more than one parent class. Go back to the `validate.py` file and add the following code:

```python
class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass
```

These new classes combine type checking and value checking. For example, the `PositiveInteger` class checks that a value is both an integer and non-negative. The order of inheritance matters here. The validators are checked in the order specified in the class definition.

## Testing the Composed Validators

Let's test our composed validators. In the Python interpreter, run the following code:

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

When you run this code, you should see:

```
10
Error: Expected <class 'int'>
Error: Expected >= 0
'hello'
Error: Must be non-empty
```

This shows how we can combine validators to create more complex validation rules.

When you're done testing, you can exit the Python interpreter by running the following command:

```python
exit()
```
