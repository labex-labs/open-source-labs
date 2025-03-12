# Creating the Basic CSV Reader Functions

Let's start by creating a `reader.py` file with two basic functions for reading CSV data. These functions will help us handle CSV files in different ways, such as converting the data into dictionaries or class instances.

First, we need to understand what a CSV file is. CSV stands for Comma-Separated Values. It's a simple file format used to store tabular data, where each line represents a row, and the values in each row are separated by commas.

Now, let's create the `reader.py` file. Follow these steps:

1. Open up the code editor and create a new file called `reader.py` in the `/home/labex/project` directory. This is where we'll write our functions to read CSV data.

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

In the `read_csv_as_dicts` function, we first open the CSV file using the `open` function. Then, we use the `csv.reader` to read the file line by line. The `next(rows)` statement reads the first line of the file, which usually contains the headers. After that, we iterate over the remaining rows. For each row, we create a dictionary where the keys are the headers and the values are the corresponding values in the row, with optional type conversion using the `types` list.

The `read_csv_as_instances` function is similar, but instead of creating dictionaries, it creates instances of a given class. It assumes that the class has a static method called `from_row` that can create an instance from a row of data.

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

In the `test_reader.py` file, we import the `reader` module that we just created and the `stock` module. We then test the two functions by calling them with a sample CSV file named `portfolio.csv`. We print the first item and the total number of items in the portfolio to verify that the functions are working as expected.

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
