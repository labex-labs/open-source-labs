# Working with Dictionaries and CSV Data

Let's start by examining a simple dataset about stock holdings. In this step, you'll learn how to read data from a CSV file and store it in a structured format using dictionaries.

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

This code defines a function `read_portfolio` that:

1. Opens a CSV file
2. Skips the header row
3. Creates a dictionary for each data row with keys for 'name', 'shares', and 'price'
4. Converts the shares to integers and prices to floating-point numbers
5. Adds each dictionary to a list
6. Returns the complete list of dictionaries

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

The `pprint` function (pretty print) displays the data in a more readable format. Each item in the list is a dictionary representing one stock holding with:

- A stock symbol (`name`)
- Number of shares owned (`shares`)
- Purchase price per share (`price`)

Notice that some stocks like 'MSFT' and 'IBM' appear multiple times - these represent different purchases of the same stock.
