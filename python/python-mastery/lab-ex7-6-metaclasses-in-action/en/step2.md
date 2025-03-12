# Collecting Validator Types

Our first task is to modify the base `Validator` class to collect all of its subclasses. This will allow us to create a namespace containing all validator types that we can later inject into the `Structure` class.

Open the `validate.py` file and add a class-level dictionary and an `__init_subclass__()` method to the `Validator` class:

```bash
code validate.py
```

Add the following code to the `Validator` class, right after the class definition:

```python
# Add this to the Validator class in validate.py
validators = {}  # Dictionary to collect all validator subclasses

@classmethod
def __init_subclass__(cls):
    """Register each validator subclass in the validators dictionary"""
    Validator.validators[cls.__name__] = cls
```

Your modified `Validator` class should now look like this:

```python
class Validator:
    validators = {}  # Dictionary to collect all validator subclasses

    @classmethod
    def __init_subclass__(cls):
        """Register each validator subclass in the validators dictionary"""
        Validator.validators[cls.__name__] = cls

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.name] = value

    def validate(self, value):
        pass
```

Now, each time a new validator type is defined (like `String` or `PositiveInteger`), it will automatically be added to the `validators` dictionary with its class name as the key.

Let's test if our code works. Create a simple Python script to check the contents of the `validators` dictionary:

```bash
python3 -c "from validate import Validator; print(Validator.validators)"
```

You should see output similar to this, showing all the validator types and their corresponding classes:

```
{'Typed': <class 'validate.Typed'>, 'Positive': <class 'validate.Positive'>, 'NonEmpty': <class 'validate.NonEmpty'>, 'String': <class 'validate.String'>, 'Integer': <class 'validate.Integer'>, 'Float': <class 'validate.Float'>, 'PositiveInteger': <class 'validate.PositiveInteger'>, 'PositiveFloat': <class 'validate.PositiveFloat'>, 'NonEmptyString': <class 'validate.NonEmptyString'>}
```

We now have a dictionary containing all of our validator types which we can use in the next step to create our metaclass.
