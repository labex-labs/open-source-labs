# Adding Method Argument Validation

Let's take our validation one step further by automatically validating method arguments. The `validate.py` file already includes a `@validated` decorator that can check function arguments against their annotations.

Let's modify our code to apply this decorator to methods with annotations:

1. Open the `validate.py` file to review the `validated` decorator:

```bash
code ~/project/validate.py
```

The `validated` decorator uses function annotations to validate arguments. It checks each argument against its annotation type before allowing the function to run.

2. Now, let's modify the `validate_attributes` function in `structure.py` to wrap annotated methods with the `validated` decorator:

```bash
code ~/project/structure.py
```

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

This updated function now:

1. Processes validator descriptors as before
2. Finds all methods with annotations
3. Applies the `@validated` decorator to those methods

4. Save the file.

5. Now, update the `sell` method in the `Stock` class to include an annotation:

```bash
code ~/project/stock.py
```

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

The important change is adding `: PositiveInteger` to the `nshares` parameter. This tells Python (and our `@validated` decorator) to validate this argument using the `PositiveInteger` validator.

7. Run the tests again to verify everything still works:

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

8. Let's test our new argument validation:

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock('GOOG', 100, 490.1); s.sell(25); print(s); try: s.sell(-25); except Exception as e: print(f'Error: {e}')"
```

You should see output similar to:

```
Stock('GOOG', 75, 490.1)
Error: Bad Arguments
  nshares: must be >= 0
```

This shows that our method argument validation is working! The first call to `sell(25)` succeeds, but the second call to `sell(-25)` fails because `-25` is not a positive integer.

You've now implemented a complete system for:

1. Validating class attributes using descriptors
2. Automatically collecting field information using class decorators
3. Converting row data to instances
4. Validating method arguments using annotations

This demonstrates the power of combining descriptors and decorators in Python to create expressive, self-validating classes.
