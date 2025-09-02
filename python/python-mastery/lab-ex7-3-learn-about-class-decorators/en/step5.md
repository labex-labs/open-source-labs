# Adding Method Argument Validation

In Python, validating data is an important part of writing robust code. In this section, we'll take our validation one step further by automatically validating method arguments. The `validate.py` file already includes a `@validated` decorator. A decorator in Python is a special function that can modify another function. The `@validated` decorator here can check function arguments against their annotations. Annotations in Python are a way to add metadata to function parameters and return values.

Let's modify our code to apply this decorator to methods with annotations:

1. First, we need to understand how the `validated` decorator works. Open the `validate.py` file in your editor to review it.

The `validated` decorator uses function annotations to validate arguments. Before allowing the function to run, it creates an instance of the validator class for each annotated parameter and calls the `validate` method to check the argument. For example, if an argument is annotated with `PositiveInteger`, the decorator will create a `PositiveInteger` instance and validate that the passed value is indeed a positive integer. If validation fails, it collects all errors and raises a `TypeError` with detailed error messages.

2. Now, we'll modify the `validate_attributes` function in `structure.py` to wrap annotated methods with the `validated` decorator. This means that any method with annotations in the class will have its arguments automatically validated. Open the `structure.py` file in your editor.

3. Update the `validate_attributes` function:

```python
def validate_attributes(cls):
    """
    Class decorator that:
    1. Extracts Validator instances and builds _fields and _types lists
    2. Applies @validated decorator to methods with annotations
    """
    # Import the validated decorator
    from validate import validated

    # Process validator descriptors
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # Set _fields based on validator names
    cls._fields = [val.name for val in validators]

    # Set _types based on validator expected_types
    cls._types = [getattr(val, 'expected_type', lambda x: x) for val in validators]

    # Apply @validated decorator to methods with annotations
    for name, val in vars(cls).items():
        if callable(val) and hasattr(val, '__annotations__'):
            setattr(cls, name, validated(val))

    # Create initialization method
    cls.create_init()

    return cls
```

This updated function now does the following:

1. It processes validator descriptors as before. Validator descriptors are used to define validation rules for class attributes.
2. It finds all methods with annotations in the class. Annotations are added to method parameters to specify the expected type of the argument.
3. It applies the `@validated` decorator to those methods. This ensures that the arguments passed to these methods are validated according to their annotations.

4. Save the file after making these changes. Saving the file is important because it makes sure that our modifications are stored and can be used later.

5. Now, let's update the `sell` method in the `Stock` class to include an annotation. Annotations help in specifying the expected type of the argument, which will be used by the `@validated` decorator for validation. Open the `stock.py` file in your editor.

6. Modify the `sell` method to include a type annotation:

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

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

The important change is adding `: PositiveInteger` to the `nshares` parameter. This tells Python (and our `@validated` decorator) to validate this argument using the `PositiveInteger` validator. So, when we call the `sell` method, the `nshares` argument must be a positive integer.

7. Run the tests again to verify everything still works. Running tests is a good way to make sure that our changes haven't broken any existing functionality.

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

8. Let's test our new argument validation. We'll try to call the `sell` method with valid and invalid arguments to see if the validation works as expected.

```bash
cd ~/project
python3 -c "
from stock import Stock
s = Stock('GOOG', 100, 490.1)
s.sell(25)
print(s)
try:
    s.sell(-25)
except Exception as e:
    print(f'Error: {e}')
"
```

You should see output similar to:

```
Stock('GOOG', 75, 490.1)
Error: Bad Arguments
  nshares: nshares must be >= 0
```

This shows that our method argument validation is working! The first call to `sell(25)` succeeds because `25` is a positive integer. But the second call to `sell(-25)` fails because `-25` is not a positive integer.

You've now implemented a complete system for:

1. Validating class attributes using descriptors. Descriptors are used to define validation rules for class attributes.
2. Automatically collecting field information using class decorators. Class decorators can modify the behavior of a class, like collecting field information.
3. Converting row data to instances. This is useful when working with data from external sources.
4. Validating method arguments using annotations. Annotations help in specifying the expected type of the argument for validation.

This demonstrates the power of combining descriptors and decorators in Python to create expressive, self-validating classes.
