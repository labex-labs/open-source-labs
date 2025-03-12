# Using the map() Function

Python's `map()` function is another example of a higher-order function. It applies a given function to each item in an iterable and returns an iterator of results. This makes it perfect for processing sequences of data, like rows in a CSV file.

The basic syntax of `map()` is:

```python
map(function, iterable, ...)
```

For example, to square each number in a list:

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x * x, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
```

Now, let's modify our `convert_csv()` function to use `map()` instead of a for loop:

```python
def convert_csv(lines, conversion_func, *, headers=None):
    '''
    Convert lines of CSV data using the provided conversion function
    '''
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)

    # Use map to apply conversion_func to each row
    records = list(map(lambda row: conversion_func(headers, row), rows))
    return records
```

This version does exactly the same thing as before, but uses `map()` instead of a for loop. The lambda function takes each row and applies `conversion_func` to it, along with the headers.

Let's test this updated function to make sure it works correctly:

```bash
cd ~/project
python3 -i reader.py
```

In the Python shell, run:

```python
# Test the updated convert_csv function
with open('portfolio.csv') as f:
    result = convert_csv(f, make_dict)
print(result[0])  # Should print the first dictionary

# Test that csv_as_dicts still works
with open('portfolio.csv') as f:
    portfolio = csv_as_dicts(f, [str, int, float])
print(portfolio[0])  # Should print the first dictionary with converted types
```

You should see output similar to:

```
{'name': 'AA', 'shares': '100', 'price': '32.20'}
{'name': 'AA', 'shares': 100, 'price': 32.2}
```

The updated `convert_csv()` function using `map()` works correctly, and the functions that rely on it also continue to work.

Using `map()` has several advantages:

1. It can be more concise than a for loop
2. It clearly communicates your intent to transform each item in a sequence
3. It can be more memory-efficient because it returns an iterator (though we convert it to a list in this case)

Exit the Python shell by typing `exit()` or pressing Ctrl+D.
