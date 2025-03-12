# Creating a Utility Function for CSV Processing

Now that we understand how Python's first-class objects can help us with data conversion, we're going to create a reusable utility function. This function will read CSV data and transform it into a list of dictionaries. This is a very useful operation because CSV files are commonly used to store tabular data, and converting them into a list of dictionaries makes it easier to work with the data in Python.

## Creating the CSV Reader Utility

First, open the WebIDE. Once it's open, navigate to the project directory and create a new file named `reader.py`. In this file, we'll define a function that reads CSV data and applies type conversions. Type conversions are important because the data in a CSV file is usually read as strings, but we might need different data types like integers or floating-point numbers for further processing.

Add the following code to `reader.py`:

```python
import csv

def read_csv_as_dicts(filename, types):
    """
    Read a CSV file into a list of dictionaries, converting each field according
    to the types provided.

    Parameters:
    filename (str): Name of the CSV file to read
    types (list): List of type conversion functions for each column

    Returns:
    list: List of dictionaries representing the CSV data
    """
    records = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)  # Get the column headers

        for row in rows:
            # Apply type conversions to each value in the row
            converted_row = [func(val) for func, val in zip(types, row)]

            # Create a dictionary mapping headers to converted values
            record = dict(zip(headers, converted_row))
            records.append(record)

    return records
```

This function first opens the specified CSV file. It then reads the headers of the CSV file, which are the names of the columns. After that, it goes through each row in the file. For each value in the row, it applies the corresponding type conversion function from the `types` list. Finally, it creates a dictionary where the keys are the column headers and the values are the converted data, and adds this dictionary to the `records` list. Once all rows are processed, it returns the `records` list.

## Testing the Utility Function

Let's test our utility function. First, open a terminal and start a Python interpreter by typing:

```bash
python3
```

Now that we're in the Python interpreter, we can use our function to read the portfolio data. The portfolio data is a CSV file that contains information about stocks, such as the name of the stock, the number of shares, and the price.

```python
import reader
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
for record in portfolio[:3]:  # Show the first 3 records
    print(record)
```

When you run this code, you should see output similar to:

```
{'name': 'AA', 'shares': 100, 'price': 32.2}
{'name': 'IBM', 'shares': 50, 'price': 91.1}
{'name': 'CAT', 'shares': 150, 'price': 83.44}
```

This output shows the first three records from the portfolio data, with the data types correctly converted.

Let's also try our function with the CTA bus data. The CTA bus data is another CSV file that contains information about bus routes, dates, day types, and the number of rides.

```python
rows = reader.read_csv_as_dicts('ctabus.csv', [str, str, str, int])
print(f"Total rows: {len(rows)}")
print("First row:", rows[0])
```

The output should be something like:

```
Total rows: 577563
First row: {'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
```

This shows that our function can handle different CSV files and apply the appropriate type conversions.

To exit the Python interpreter, type:

```python
exit()
```

You've now created a reusable utility function that can read any CSV file and apply appropriate type conversions. This demonstrates the power of Python's first-class objects and how they can be used to create flexible, reusable code.
