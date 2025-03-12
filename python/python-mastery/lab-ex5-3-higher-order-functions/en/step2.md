# Creating a Higher-Order Function

In Python, a higher-order function is a function that can take another function as an argument. This allows for greater flexibility and code reuse. Now, let's create a higher-order function called `convert_csv()`. This function will handle the common operations of processing CSV data, while allowing you to customize how each row of the CSV is converted into a record.

Open the `reader.py` file in the WebIDE. We're going to add a function that will take an iterable of CSV data, a conversion function, and optionally, column headers. The conversion function will be used to transform each row of the CSV into a record.

Here's the code for the `convert_csv()` function. Copy and paste it into your `reader.py` file:

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

Let's break down what this function does. First, it initializes an empty list called `records` to store the converted records. Then, it uses the `csv.reader()` function to read the lines of CSV data. If no headers are provided, it takes the first row as the headers. For each subsequent row, it applies the `conversion_func` to convert the row into a record and adds it to the `records` list. Finally, it returns the list of records.

Now, we need a simple conversion function to test our `convert_csv()` function. This function will take the headers and a row and convert the row into a dictionary using the headers as keys.

Here's the code for the `make_dict()` function. Add this function to your `reader.py` file as well:

```python
def make_dict(headers, row):
    '''
    Convert a row to a dictionary using the provided headers
    '''
    return dict(zip(headers, row))
```

The `make_dict()` function uses the `zip()` function to pair each header with its corresponding value in the row, and then creates a dictionary from these pairs.

Let's test these functions. Open a Python shell by running the following commands in the terminal:

```bash
cd ~/project
python3 -i reader.py
```

The `-i` option in the `python3` command starts the Python interpreter in interactive mode and imports the `reader.py` file, so we can use the functions we just defined.

In the Python shell, run the following code to test our functions:

```python
# Open the CSV file
lines = open('portfolio.csv')

# Convert to a list of dictionaries using our new function
result = convert_csv(lines, make_dict)

# Print the result
print(result)
```

This code opens the `portfolio.csv` file, uses the `convert_csv()` function with the `make_dict()` conversion function to convert the CSV data into a list of dictionaries, and then prints the result.

You should see output similar to the following:

```
[{'name': 'AA', 'shares': '100', 'price': '32.20'}, {'name': 'IBM', 'shares': '50', 'price': '91.10'}, {'name': 'CAT', 'shares': '150', 'price': '83.44'}, {'name': 'MSFT', 'shares': '200', 'price': '51.23'}, {'name': 'GE', 'shares': '95', 'price': '40.37'}, {'name': 'MSFT', 'shares': '50', 'price': '65.10'}, {'name': 'IBM', 'shares': '100', 'price': '70.44'}]
```

This output shows that our higher-order function `convert_csv()` works correctly. We've successfully created a function that takes another function as an argument, which gives us the ability to easily change how the CSV data is converted.

To exit the Python shell, you can type `exit()` or press Ctrl+D.
