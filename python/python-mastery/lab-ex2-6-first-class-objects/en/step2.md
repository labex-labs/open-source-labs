# Creating a Utility Function for CSV Processing

Now that we understand how Python's first-class objects can help us with data conversion, let's create a reusable utility function that reads CSV data into a list of dictionaries.

## Creating the CSV Reader Utility

Open the WebIDE and create a new file named `reader.py` in the project directory. In this file, we'll define a function that reads CSV data and applies type conversions.

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

This function reads a CSV file, applies the specified type conversions to each column, and returns a list of dictionaries where keys are column headers and values are the converted data.

## Testing the Utility Function

Let's test our utility function by opening a Python interpreter and using it to read the portfolio data. Open a terminal and type:

```bash
python3
```

Now, use the function to read the portfolio data:

```python
import reader
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
for record in portfolio[:3]:  # Show the first 3 records
    print(record)
```

You should see output similar to:

```
{'name': 'AA', 'shares': 100, 'price': 32.2}
{'name': 'IBM', 'shares': 50, 'price': 91.1}
{'name': 'CAT', 'shares': 150, 'price': 83.44}
```

Let's also try it with the CTA bus data:

```python
rows = reader.read_csv_as_dicts('ctabus.csv', [str, str, str, int])
print(f"Total rows: {len(rows)}")
print("First row:", rows[0])
```

Output:

```
Total rows: 577563
First row: {'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
```

Exit the Python interpreter by typing:

```python
exit()
```

You've now created a reusable utility function that can read any CSV file and apply appropriate type conversions. This demonstrates the power of Python's first-class objects and how they can be used to create flexible, reusable code.
