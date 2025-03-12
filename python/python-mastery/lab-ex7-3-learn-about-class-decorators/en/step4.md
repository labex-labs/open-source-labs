# Adding Row Conversion Functionality

Now let's add the ability to create instances from data rows, which is useful for reading data from CSV files. We'll implement a `from_row` class method in the `Structure` class.

1. Open the `structure.py` file:

```bash
code ~/project/structure.py
```

2. First, modify the `validate_attributes` function to collect type information:

```python
def validate_attributes(cls):
    """
    Class decorator that extracts Validator instances
    and builds the _fields and _types lists automatically
    """
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    # Set _fields based on validator names
    cls._fields = [val.name for val in validators]

    # Set _types based on validator expected_types
    cls._types = [getattr(val, 'expected_type', lambda x: x) for val in validators]

    # Create initialization method
    cls.create_init()

    return cls
```

This updated function now also collects the `expected_type` attribute from each validator and stores it in the `_types` class variable.

3. Now, add the `from_row` class method to the `Structure` class:

```python
@classmethod
def from_row(cls, row):
    """
    Create an instance from a data row (list or tuple)
    """
    rowdata = [func(val) for func, val in zip(cls._types, row)]
    return cls(*rowdata)
```

This method:

- Takes a row of data (like a list or tuple)
- Converts each value to the expected type using the corresponding function from `_types`
- Creates and returns a new instance using the converted values

4. Save the file.

5. Let's create a simple test to verify that our `from_row` method works:

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock.from_row(['GOOG', '100', '490.1']); print(s); print(f'Cost: {s.cost}')"
```

You should see output similar to:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

Notice how the string values '100' and '490.1' were automatically converted to the correct types (integer and float).

6. Now let's try reading data from a CSV file using our `reader.py` module:

```bash
cd ~/project
python3 -c "from stock import Stock; import reader; portfolio = reader.read_csv_as_instances('portfolio.csv', Stock); print(portfolio); print(f'Total value: {sum(s.cost for s in portfolio)}')"
```

You should see output showing the stocks from the CSV file:

```
[Stock('GOOG', 100, 490.1), Stock('AAPL', 50, 545.75), Stock('MSFT', 200, 30.47)]
Total value: 73444.0
```

The `from_row` method allows us to easily convert CSV data into instances. Combined with the `read_csv_as_instances` function, we now have a powerful way to load and work with structured data.
