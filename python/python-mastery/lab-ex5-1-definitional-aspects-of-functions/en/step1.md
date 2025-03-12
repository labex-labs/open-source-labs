# Understanding the Context

In earlier exercises, you might have worked with code for reading CSV files into different data structures. This code typically transforms raw text data into more useful Python objects like dictionaries or class instances.

The typical pattern for reading CSV files often looks like this:

```python
import csv

def read_csv_as_dicts(filename, types):
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = { name: func(val)
                       for name, func, val in zip(headers, types, row) }
            records.append(record)
    return records
```

This function reads a CSV file and converts each row into a dictionary, applying type conversions using the functions provided in the `types` list.

A similar function might read data into class instances:

```python
def read_csv_as_instances(filename, cls):
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = cls.from_row(row)
            records.append(record)
    return records
```

In this lab, we'll refactor these functions to make them more flexible and robust, while also exploring Python's type hinting system.

Let's start by creating a `reader.py` file with these initial functions and making sure they work properly.
