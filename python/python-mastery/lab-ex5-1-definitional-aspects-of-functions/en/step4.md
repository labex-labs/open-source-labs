# Handling CSV Files Without Headers

Not all CSV files include headers in their first row. Let's modify our functions to handle files without headers by allowing the caller to provide the headers manually.

1. Open the `reader.py` file and update it to include header handling:

```python
# reader.py

import csv

def csv_as_dicts(lines, types, headers=None):
    '''
    Parse CSV data from an iterable into a list of dictionaries

    Args:
        lines: An iterable producing CSV lines
        types: List of type conversion functions for each column
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of dictionaries with data from the CSV lines
    '''
    records = []
    rows = csv.reader(lines)

    if headers is None:
        # Use the first row as headers if none provided
        headers = next(rows)

    for row in rows:
        record = { name: func(val)
                  for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines, cls, headers=None):
    '''
    Parse CSV data from an iterable into a list of class instances

    Args:
        lines: An iterable producing CSV lines
        cls: Class to create instances from
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of class instances with data from the CSV lines
    '''
    records = []
    rows = csv.reader(lines)

    if headers is None:
        # Skip the first row if no headers provided
        next(rows)

    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_dicts(filename, types, headers=None):
    '''
    Read CSV data into a list of dictionaries with optional type conversion

    Args:
        filename: Path to the CSV file
        types: List of type conversion functions for each column
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of dictionaries with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types, headers)

def read_csv_as_instances(filename, cls, headers=None):
    '''
    Read CSV data into a list of class instances

    Args:
        filename: Path to the CSV file
        cls: Class to create instances from
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of class instances with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls, headers)
```

The key changes are:

1. Adding a `headers` parameter to all functions, defaulting to `None`
2. Using the first row as headers only if `headers` is `None`
3. Skipping the first row in `csv_as_instances` only if `headers` is `None`

4. Let's test these modifications with our file without headers. Create a file called `test_headers.py`:

```python
# test_headers.py

import reader
import stock

# Define column names for the file without headers
column_names = ['name', 'shares', 'price']

# Test reading a file without headers
portfolio = reader.read_csv_as_dicts('portfolio_noheader.csv',
                                     [str, int, float],
                                     headers=column_names)
print("First item from file without headers:", portfolio[0])
print("Total items:", len(portfolio))

# Test reading the same file as instances
portfolio = reader.read_csv_as_instances('portfolio_noheader.csv',
                                        stock.Stock,
                                        headers=column_names)
print("\nFirst item as Stock instance:", portfolio[0])
print("Total items:", len(portfolio))

# Verify that original functionality still works
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("\nFirst item from file with headers:", portfolio[0])
```

3. Run the test script from the terminal:

```bash
python test_headers.py
```

The output should look similar to:

```
First item from file without headers: {'name': 'AA', 'shares': 100, 'price': 32.2}
Total items: 7

First item as Stock instance: Stock('AA', 100, 32.2)
Total items: 7

First item from file with headers: {'name': 'AA', 'shares': 100, 'price': 32.2}
```

This confirms that our functions can now handle CSV files both with and without headers. The user can provide column names when needed, or rely on the default behavior of reading headers from the first row.

By making this modification, our CSV reader functions are now more versatile and can handle a wider range of file formats.
