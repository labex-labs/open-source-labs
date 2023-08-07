# Row Conversion

One missing feature from the `Structure` class is a `from_row()` method that
allows it to work with earlier CSV reading code. Let's fix that. Give the
`Structure` class a `_types` class variable and the following class method:

```python
# structure.py

class Structure:
    _types = ()
    ...
    @classmethod
    def from_row(cls, row):
        rowdata = [ func(val) for func, val in zip(cls._types, row) ]
        return cls(*rowdata)
    ...
```

Modify the `@validate_attributes` decorator so that it examines the
various validators for an `expected_type` attribute and uses it to
fill in the `_types` variable above.

Once you've done this, you should be able to do things like this:

```python
>>> s = Stock.from_row(['GOOG', '100', '490.1'])
>>> s
Stock('GOOG', 100, 490.1)
>>> import reader
>>> port = reader.read_csv_as_instances('portfolio.csv', Stock)
>>>
```
