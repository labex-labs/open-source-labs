# Adding Row Conversion Functionality

In programming, it's often useful to create instances of a class from data rows, especially when dealing with data from sources like CSV files. In this section, we'll add the ability to create instances of the `Structure` class from data rows. We'll do this by implementing a `from_row` class method in the `Structure` class.

1. First, open the `structure.py` file in your editor. This is where we'll make our code changes.

2. Next, we'll modify the `validate_attributes` function. This function is a class decorator that extracts `Validator` instances and builds the `_fields` and `_types` lists automatically. We'll update it to also collect type information.

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

In this updated function, we're collecting the `expected_type` attribute from each validator and storing it in the `_types` class variable. This will be useful later when we convert data from rows to the correct types.

3. Now, we'll add the `from_row` class method to the `Structure` class. This method will allow us to create an instance of the class from a data row, which could be a list or a tuple.

```python
@classmethod
def from_row(cls, row):
    """
    Create an instance from a data row (list or tuple)
    """
    rowdata = [func(val) for func, val in zip(cls._types, row)]
    return cls(*rowdata)
```

Here's how this method works:

- It takes a row of data, which can be in the form of a list or a tuple.
- It converts each value in the row to the expected type using the corresponding function from the `_types` list.
- It then creates and returns a new instance of the class using the converted values.

4. After making these changes, save the `structure.py` file. This ensures that your code changes are preserved.

5. Let's test our `from_row` method to make sure it works as expected. We'll create a simple test using the `Stock` class. Run the following command in your terminal:

```bash
cd ~/project
python3 -c "from stock import Stock; s = Stock.from_row(['GOOG', '100', '490.1']); print(s); print(f'Cost: {s.cost}')"
```

You should see output similar to this:

```
Stock('GOOG', 100, 490.1)
Cost: 49010.0
```

Notice that the string values '100' and '490.1' were automatically converted to the correct types (integer and float). This shows that our `from_row` method is working correctly.

6. Finally, let's try reading data from a CSV file using our `reader.py` module. Run the following command in your terminal:

```bash
cd ~/project
python3 -c "from stock import Stock; import reader; portfolio = reader.read_csv_as_instances('portfolio.csv', Stock); print(portfolio); print(f'Total value: {sum(s.cost for s in portfolio)}')"
```

You should see output showing the stocks from the CSV file:

```
[Stock('GOOG', 100, 490.1), Stock('AAPL', 50, 545.75), Stock('MSFT', 200, 30.47)]
Total value: 82391.5
```

The `from_row` method allows us to easily convert CSV data into instances of the `Stock` class. When combined with the `read_csv_as_instances` function, we have a powerful way to load and work with structured data.
