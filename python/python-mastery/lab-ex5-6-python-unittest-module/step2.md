# Unit testing

Using the code in `teststock.py` as a guide, extend the `TestStock` class with tests for the following:

- Test that you can create a `Stock` using keyword arguments such as `Stock(name='GOOG',shares=100,price=490.1)`.
- Test that the `cost` property returns a correct value
- Test that the `sell()` method correctly updates the shares.
- Test that the `from_row()` class method creates a new instance from good data.
- Test that the `__repr__()` method creates a proper representation string.
- Test the comparison operator method `__eq__()`
