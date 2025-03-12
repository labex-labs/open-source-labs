# Working with Dictionaries and CSV Data

Let's start by examining a simple dataset about stock holdings. In this step, you'll learn how to read data from a CSV file and store it in a structured format using dictionaries.

A CSV (Comma-Separated Values) file is a common way to store tabular data, where each line represents a row and values are separated by commas. Dictionaries in Python are a powerful data structure that allow you to store key - value pairs. By using dictionaries, we can organize the data from the CSV file in a more meaningful way.

First, create a new Python file in the WebIDE by following these steps:

1. Click on the "New File" button in the WebIDE
2. Name the file `readport.py`
3. Copy and paste the following code into the file:

```python
# readport.py

import csv

# A function that reads a file into a list of dictionaries
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)   # Skip the header row
        for row in rows:
            record = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(record)
    return portfolio
```

This code defines a function `read_portfolio` that performs several important tasks:

1. It opens a CSV file specified by the `filename` parameter. The `open` function is used to access the file, and the `with` statement ensures that the file is properly closed after we're done reading it.
2. It skips the header row. The header row usually contains the names of the columns in the CSV file. We use `next(rows)` to move the iterator to the next row, effectively skipping the header.
3. For each data row, it creates a dictionary. The keys of the dictionary are 'name', 'shares', and 'price'. These keys will help us access the data in a more intuitive way.
4. It converts the shares to integers and prices to floating - point numbers. This is important because the data read from the CSV file is initially in string format, and we need numerical values for calculations.
5. It adds each dictionary to a list called `portfolio`. This list will contain all the records from the CSV file.
6. Finally, it returns the complete list of dictionaries.

Now let's create a file for the transit data. Create a new file called `readrides.py` with this content:

```python
# readrides.py

import csv

def read_rides_as_dicts(filename):
    """
    Read the CTA bus data as a list of dictionaries
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)   # Skip header
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides
            }
            records.append(record)
    return records
```

This `read_rides_as_dicts` function works in a similar way to the `read_portfolio` function. It reads a CSV file related to CTA bus data, skips the header row, creates a dictionary for each data row, and stores these dictionaries in a list.

Now, let's test the `read_portfolio` function by opening a terminal in the WebIDE:

1. Click on the "Terminal" menu and select "New Terminal"
2. Start the Python interpreter by typing `python3`
3. Execute the following commands:

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> from pprint import pprint
>>> pprint(portfolio)
[{'name': 'AA', 'price': 32.2, 'shares': 100},
 {'name': 'IBM', 'price': 91.1, 'shares': 50},
 {'name': 'CAT', 'price': 83.44, 'shares': 150},
 {'name': 'MSFT', 'price': 51.23, 'shares': 200},
 {'name': 'GE', 'price': 40.37, 'shares': 95},
 {'name': 'MSFT', 'price': 65.1, 'shares': 50},
 {'name': 'IBM', 'price': 70.44, 'shares': 100}]
```

The `pprint` function (pretty print) is used here to display the data in a more readable format. Each item in the list is a dictionary representing one stock holding. The dictionary has the following keys:

- A stock symbol (`name`): This is the abbreviation used to identify the stock.
- Number of shares owned (`shares`): This indicates how many shares of the stock are held.
- Purchase price per share (`price`): This is the price at which each share was bought.

Notice that some stocks like 'MSFT' and 'IBM' appear multiple times. These represent different purchases of the same stock, which might have been made at different times and prices.
