# Collecting Validator Types

In Python, validators are classes that help us ensure that data meets certain criteria. Our first task in this experiment is to modify the base `Validator` class so that it can collect all of its subclasses. Why do we need to do this? Well, by collecting all validator subclasses, we can create a namespace that contains all validator types. Later, we'll inject this namespace into the `Structure` class, which will make it easier for us to manage and use different validators.

Now, let's start working on the code. Open the `validate.py` file. You can use the following command in the terminal to open it:

```bash
code validate.py
```

Once the file is open, we need to add a class - level dictionary and an `__init_subclass__()` method to the `Validator` class. The class - level dictionary will be used to store all the validator subclasses, and the `__init_subclass__()` method is a special method in Python that gets called every time a subclass of the current class is defined.

Add the following code to the `Validator` class, right after the class definition:

```python
# Add this to the Validator class in validate.py
validators = {}  # Dictionary to collect all validator subclasses

@classmethod
def __init_subclass__(cls):
    """Register each validator subclass in the validators dictionary"""
    Validator.validators[cls.__name__] = cls
```

After adding the code, your modified `Validator` class should now look like this:

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

Now, every time a new validator type is defined, like `String` or `PositiveInteger`, Python will automatically call the `__init_subclass__()` method. This method will then add the new validator subclass to the `validators` dictionary, using the class name as the key.

Let's test if our code works. We'll create a simple Python script to check the contents of the `validators` dictionary. You can run the following command in the terminal:

```bash
python3 -c "from validate import Validator; print(Validator.validators)"
```

If everything works correctly, you should see output similar to this, showing all the validator types and their corresponding classes:

```
{'Typed': <class 'validate.Typed'>, 'Positive': <class 'validate.Positive'>, 'NonEmpty': <class 'validate.NonEmpty'>, 'String': <class 'validate.String'>, 'Integer': <class 'validate.Integer'>, 'Float': <class 'validate.Float'>, 'PositiveInteger': <class 'validate.PositiveInteger'>, 'PositiveFloat': <class 'validate.PositiveFloat'>, 'NonEmptyString': <class 'validate.NonEmptyString'>}
```

Now that we have a dictionary containing all of our validator types, we can use it in the next step to create our metaclass.
