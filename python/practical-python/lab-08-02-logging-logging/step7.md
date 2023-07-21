# Exercise 8.2: Adding logging to a module

In `fileparse.py`, there is some error handling related to
exceptions caused by bad input. It looks like this:

```python
# fileparse.py
import csv

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records with type conversion.
    '''
    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    rows = csv.reader(lines, delimiter=delimiter)

    # Read the file headers (if any)
    headers = next(rows) if has_headers else []

    # If specific columns have been selected, make indices for filtering and set output columns
    if select:
        indices = [ headers.index(colname) for colname in select ]
        headers = select

    records = []
    for rowno, row in enumerate(rows, 1):
        if not row:     # Skip rows with no data
            continue

        # If specific column indices are selected, pick them out
        if select:
            row = [ row[index] for index in indices]

        # Apply type conversion to the row
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {rowno}: Couldn't convert {row}")
                    print(f"Row {rowno}: Reason {e}")
                continue

        # Make a dictionary or a tuple
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
```

Notice the print statements that issue diagnostic messages. Replacing those
prints with logging operations is relatively simple. Change the code like this:

```python
# fileparse.py
import csv
import logging
log = logging.getLogger(__name__)

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records with type conversion.
    '''
    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    rows = csv.reader(lines, delimiter=delimiter)

    # Read the file headers (if any)
    headers = next(rows) if has_headers else []

    # If specific columns have been selected, make indices for filtering and set output columns
    if select:
        indices = [ headers.index(colname) for colname in select ]
        headers = select

    records = []
    for rowno, row in enumerate(rows, 1):
        if not row:     # Skip rows with no data
            continue

        # If specific column indices are selected, pick them out
        if select:
            row = [ row[index] for index in indices]

        # Apply type conversion to the row
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    log.warning("Row %d: Couldn't convert %s", rowno, row)
                    log.debug("Row %d: Reason %s", rowno, e)
                continue

        # Make a dictionary or a tuple
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
```

Now that you've made these changes, try using some of your code on
bad data.

```python
>>> import report
>>> a = report.read_portfolio('Data/missing.csv')
Row 4: Bad row: ['MSFT', '', '51.23']
Row 7: Bad row: ['IBM', '', '70.44']
>>>
```

If you do nothing, you'll only get logging messages for the `WARNING`
level and above. The output will look like simple print statements.
However, if you configure the logging module, you'll get additional
information about the logging levels, module, and more. Type these
steps to see that:

```python
>>> import logging
>>> logging.basicConfig()
>>> a = report.read_portfolio('Data/missing.csv')
WARNING:fileparse:Row 4: Bad row: ['MSFT', '', '51.23']
WARNING:fileparse:Row 7: Bad row: ['IBM', '', '70.44']
>>>
```

You will notice that you don't see the output from the `log.debug()`
operation. Type this to change the level.

```python
>>> logging.getLogger('fileparse').setLevel(logging.DEBUG)
>>> a = report.read_portfolio('Data/missing.csv')
WARNING:fileparse:Row 4: Bad row: ['MSFT', '', '51.23']
DEBUG:fileparse:Row 4: Reason: invalid literal for int() with base 10: ''
WARNING:fileparse:Row 7: Bad row: ['IBM', '', '70.44']
DEBUG:fileparse:Row 7: Reason: invalid literal for int() with base 10: ''
>>>
```

Turn off all, but the most critical logging messages:

```python
>>> logging.getLogger('fileparse').setLevel(logging.CRITICAL)
>>> a = report.read_portfolio('Data/missing.csv')
>>>
```
