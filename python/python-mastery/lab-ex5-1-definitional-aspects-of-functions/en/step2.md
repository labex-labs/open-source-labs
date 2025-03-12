# Creating the Basic CSV Reader Functions

Let's start by creating a `reader.py` file with two basic functions for reading CSV data. Follow these steps:

1. Open up the code editor and create a new file called `reader.py` in the `/home/labex/project` directory.

2. Add the following code to `reader.py`:

```python
# reader.py

import csv

def read_csv_as_dicts(filename, types):
    '''
    Read CSV data into a list of dictionaries with optional type conversion

    Args:
        filename: Path to the CSV file
        types: List of type conversion functions for each column

    Returns:
        List of dictionaries with data from the CSV file
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = { name: func(val)
                       for name, func, val in zip(headers, types, row) }
            records.append(record)
    return records

def read_csv_as_instances(filename, cls):
    '''
    Read CSV data into a list of class instances

    Args:
        filename: Path to the CSV file
        cls: Class to create instances from

    Returns:
        List of class instances with data from the CSV file
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = cls.from_row(row)
            records.append(record)
    return records
```

3. Let's test these functions to make sure they work correctly. Create a new file called `test_reader.py` with the following code:

```python
# test_reader.py

import reader
import stock

# Test reading CSV as dictionaries
portfolio_dicts = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("First portfolio item as dictionary:", portfolio_dicts[0])
print("Total items:", len(portfolio_dicts))

# Test reading CSV as class instances
portfolio_instances = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
print("\nFirst portfolio item as Stock instance:", portfolio_instances[0])
print("Total items:", len(portfolio_instances))
```

4. Run the test script from the terminal:

```bash
python test_reader.py
```

The output should look similar to this:

```
First portfolio item as dictionary: {'name': 'AA', 'shares': 100, 'price': 32.2}
Total items: 7

First portfolio item as Stock instance: Stock('AA', 100, 32.2)
Total items: 7
```

This confirms that our two functions are working correctly. The first function converts CSV data into a list of dictionaries with proper type conversion, and the second function creates class instances using a static method on the provided class.

In the next step, we'll refactor these functions to make them more flexible by allowing them to work with any iterable source of data, not just filenames.
