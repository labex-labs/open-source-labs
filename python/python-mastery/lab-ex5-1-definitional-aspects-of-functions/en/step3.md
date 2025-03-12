# Making Functions More Flexible

Currently, our functions can only read from files specified by a filename. It would be more flexible if they could work with any iterable that produces lines, such as file objects or other sources.

Let's refactor our code to enable this flexibility:

1. Open the `reader.py` file and modify it to include the following new functions:

```python
# reader.py

import csv

def csv_as_dicts(lines, types):
    '''
    Parse CSV data from an iterable into a list of dictionaries

    Args:
        lines: An iterable producing CSV lines
        types: List of type conversion functions for each column

    Returns:
        List of dictionaries with data from the CSV lines
    '''
    records = []
    rows = csv.reader(lines)
    headers = next(rows)
    for row in rows:
        record = { name: func(val)
                  for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines, cls):
    '''
    Parse CSV data from an iterable into a list of class instances

    Args:
        lines: An iterable producing CSV lines
        cls: Class to create instances from

    Returns:
        List of class instances with data from the CSV lines
    '''
    records = []
    rows = csv.reader(lines)
    headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_dicts(filename, types):
    '''
    Read CSV data into a list of dictionaries with optional type conversion

    Args:
        filename: Path to the CSV file
        types: List of type conversion functions for each column

    Returns:
        List of dictionaries with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types)

def read_csv_as_instances(filename, cls):
    '''
    Read CSV data into a list of class instances

    Args:
        filename: Path to the CSV file
        cls: Class to create instances from

    Returns:
        List of class instances with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls)
```

Notice how we've refactored the code by:

1. Creating more generic functions `csv_as_dicts()` and `csv_as_instances()` that work with any iterable
2. Reimplementing `read_csv_as_dicts()` and `read_csv_as_instances()` to use these new functions
3. This maintains backward compatibility with existing code while making our library more flexible

4. Let's test these new functions. Create a file called `test_reader_flexibility.py` with the following code:

```python
# test_reader_flexibility.py

import reader
import stock
import gzip

# Test opening a regular file
with open('portfolio.csv') as file:
    portfolio = reader.csv_as_dicts(file, [str, int, float])
    print("First item from open file:", portfolio[0])

# Test opening a gzipped file
with gzip.open('portfolio.csv.gz', 'rt') as file:  # 'rt' means read text
    portfolio = reader.csv_as_instances(file, stock.Stock)
    print("\nFirst item from gzipped file:", portfolio[0])

# Test backward compatibility
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("\nFirst item using backward compatible function:", portfolio[0])
```

3. Run the test script from the terminal:

```bash
python test_reader_flexibility.py
```

The output should look similar to:

```
First item from open file: {'name': 'AA', 'shares': 100, 'price': 32.2}

First item from gzipped file: Stock('AA', 100, 32.2)

First item using backward compatible function: {'name': 'AA', 'shares': 100, 'price': 32.2}
```

This confirms that our functions now work with different types of input sources while maintaining backward compatibility. The refactored functions can process data from:

- Regular files opened with `open()`
- Compressed files opened with `gzip.open()`
- Any other iterable object that produces lines of text

This makes our code much more flexible and easier to use in different scenarios.
