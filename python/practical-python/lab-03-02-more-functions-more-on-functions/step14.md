# Exercise 3.4: Building a Column Selector

In many cases, you're only interested in selected columns from a CSV file, not all of the data. Modify the `parse_csv()` function so that it optionally allows user-specified columns to be picked out as follows:

```python
>>> # Read all of the data
>>> portfolio = parse_csv('portfolio.csv')
>>> portfolio
[{'price': '32.20', 'name': 'AA', 'shares': '100'}, {'price': '91.10', 'name': 'IBM', 'shares': '50'}, {'price': '83.44', 'name': 'CAT', 'shares': '150'}, {'price': '51.23', 'name': 'MSFT', 'shares': '200'}, {'price': '40.37', 'name': 'GE', 'shares': '95'}, {'price': '65.10', 'name': 'MSFT', 'shares': '50'}, {'price': '70.44', 'name': 'IBM', 'shares': '100'}]

>>> # Read only some of the data
>>> shares_held = parse_csv('portfolio.csv', select=['name','shares'])
>>> shares_held
[{'name': 'AA', 'shares': '100'}, {'name': 'IBM', 'shares': '50'}, {'name': 'CAT', 'shares': '150'}, {'name': 'MSFT', 'shares': '200'}, {'name': 'GE', 'shares': '95'}, {'name': 'MSFT', 'shares': '50'}, {'name': 'IBM', 'shares': '100'}]
>>>
```

An example of a column selector was given in Exercise 2.23. However, here's one way to do it:

```python
# fileparse.py
import csv

def parse_csv(filename, select=None):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [ row[index] for index in indices ]

            # Make a dictionary
            record = dict(zip(headers, row))
            records.append(record)

    return records
```

There are a number of tricky bits to this part. Probably the most important one is the mapping of the column selections to row indices. For example, suppose the input file had the following headers:

```python
>>> headers = ['name', 'date', 'time', 'shares', 'price']
>>>
```

Now, suppose the selected columns were as follows:

```python
>>> select = ['name', 'shares']
>>>
```

To perform the proper selection, you have to map the selected column names to column indices in the file. That's what this step is doing:

```python
>>> indices = [headers.index(colname) for colname in select ]
>>> indices
[0, 3]
>>>
```

In other words, "name" is column 0 and "shares" is column 3. When you read a row of data from the file, the indices are used to filter it:

```python
>>> row = ['AA', '6/11/2007', '9:50am', '100', '32.20' ]
>>> row = [ row[index] for index in indices ]
>>> row
['AA', '100']
>>>
```
