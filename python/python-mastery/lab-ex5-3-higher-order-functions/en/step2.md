# Creating a Higher-Order Function

Now, let's create a higher-order function called `convert_csv()` that will take a conversion function as an argument. This function will handle the common operations while allowing customization of how rows are converted to records.

Open `reader.py` in the WebIDE and add the following function:

```python
def convert_csv(lines, conversion_func, *, headers=None):
    '''
    Convert lines of CSV data using the provided conversion function

    Args:
        lines: An iterable containing CSV data
        conversion_func: A function that takes headers and a row and returns a record
        headers: Column headers (optional). If None, the first row is used as headers

    Returns:
        A list of records as processed by conversion_func
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = conversion_func(headers, row)
        records.append(record)
    return records
```

Now, let's create a simple conversion function to test with `convert_csv()`:

```python
def make_dict(headers, row):
    '''
    Convert a row to a dictionary using the provided headers
    '''
    return dict(zip(headers, row))
```

Add this function to your `reader.py` file as well.

Let's test these functions by opening a Python shell:

```bash
cd ~/project
python3 -i reader.py
```

In the Python shell, run the following:

```python
# Open the CSV file
lines = open('portfolio.csv')

# Convert to a list of dictionaries using our new function
result = convert_csv(lines, make_dict)

# Print the result
print(result)
```

You should see output similar to:

```
[{'name': 'AA', 'shares': '100', 'price': '32.20'}, {'name': 'IBM', 'shares': '50', 'price': '91.10'}, {'name': 'CAT', 'shares': '150', 'price': '83.44'}, {'name': 'MSFT', 'shares': '200', 'price': '51.23'}, {'name': 'GE', 'shares': '95', 'price': '40.37'}, {'name': 'MSFT', 'shares': '50', 'price': '65.10'}, {'name': 'IBM', 'shares': '100', 'price': '70.44'}]
```

This demonstrates that our higher-order function works correctly. We've successfully created a function that takes another function as an argument.

Exit the Python shell by typing `exit()` or pressing Ctrl+D.
