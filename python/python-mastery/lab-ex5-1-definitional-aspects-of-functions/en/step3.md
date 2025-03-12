# Making Functions More Flexible

Currently, our functions are limited to reading from files specified by a filename. This restricts their usability. In programming, it's often beneficial to make functions more flexible so that they can handle different types of input. In our case, it would be great if our functions could work with any iterable that produces lines, such as file objects or other sources. This way, we can use these functions in more scenarios, like reading from compressed files or other data streams.

Let's refactor our code to enable this flexibility:

1. Open the `reader.py` file. We're going to modify it to include some new functions. These new functions will allow our code to work with different types of iterables. Here's the code you need to add:

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

Let's take a closer look at how we've refactored the code:

1. We've created two more generic functions, `csv_as_dicts()` and `csv_as_instances()`. These functions are designed to work with any iterable that produces CSV lines. This means they can handle different types of input sources, not just files specified by a filename.
2. We've reimplemented `read_csv_as_dicts()` and `read_csv_as_instances()` to use these new functions. This way, the original functionality of reading from a file by filename is still available, but now it's built on top of the more flexible functions.
3. This approach maintains backward compatibility with existing code. That means any code that was using the old functions will still work as expected. At the same time, our library becomes more flexible because it can now handle different types of input sources.

4. Now, let's test these new functions. Create a file called `test_reader_flexibility.py` and add the following code to it. This code will test the new functions with different types of input sources:

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

3. After creating the test file, we need to run the test script from the terminal. Open your terminal and navigate to the directory where the `test_reader_flexibility.py` file is located. Then run the following command:

```bash
python test_reader_flexibility.py
```

The output should look similar to this:

```
First item from open file: {'name': 'AA', 'shares': 100, 'price': 32.2}

First item from gzipped file: Stock('AA', 100, 32.2)

First item using backward compatible function: {'name': 'AA', 'shares': 100, 'price': 32.2}
```

This output confirms that our functions now work with different types of input sources while maintaining backward compatibility. The refactored functions can process data from:

- Regular files opened with `open()`
- Compressed files opened with `gzip.open()`
- Any other iterable object that produces lines of text

This makes our code much more flexible and easier to use in different scenarios.
