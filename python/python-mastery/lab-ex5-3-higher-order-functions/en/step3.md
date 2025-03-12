# Refactoring Existing Functions

Now that we have our higher-order function `convert_csv()`, let's refactor the original functions `csv_as_dicts()` and `csv_as_instances()` to use it. This will eliminate the code duplication we identified earlier.

Open `reader.py` in the WebIDE and update the functions as follows:

1. First, replace the `csv_as_dicts()` function:

```python
def csv_as_dicts(lines, types, *, headers=None):
    '''
    Convert lines of CSV data into a list of dictionaries
    '''
    def dict_converter(headers, row):
        return {name: func(val) for name, func, val in zip(headers, types, row)}

    return convert_csv(lines, dict_converter, headers=headers)
```

2. Next, replace the `csv_as_instances()` function:

```python
def csv_as_instances(lines, cls, *, headers=None):
    '''
    Convert lines of CSV data into a list of instances
    '''
    def instance_converter(headers, row):
        return cls.from_row(row)

    return convert_csv(lines, instance_converter, headers=headers)
```

Let's test these refactored functions to make sure they still work as expected. Run the following in a Python shell:

```bash
cd ~/project
python3 -i reader.py
```

In the Python shell, run:

```python
# Define a simple Stock class for testing
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        return cls(row[0], int(row[1]), float(row[2]))

    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'

# Test csv_as_dicts
with open('portfolio.csv') as f:
    portfolio_dicts = csv_as_dicts(f, [str, int, float])
print("First dictionary:", portfolio_dicts[0])

# Test csv_as_instances
with open('portfolio.csv') as f:
    portfolio_instances = csv_as_instances(f, Stock)
print("First instance:", portfolio_instances[0])
```

You should see output similar to:

```
First dictionary: {'name': 'AA', 'shares': 100, 'price': 32.2}
First instance: Stock(AA, 100, 32.2)
```

Our refactored functions are working correctly. We've successfully eliminated the code duplication while maintaining the same functionality.

Exit the Python shell by typing `exit()` or pressing Ctrl+D.
