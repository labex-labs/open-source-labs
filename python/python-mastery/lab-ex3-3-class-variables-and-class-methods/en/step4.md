# Creating a General-Purpose CSV Reader

In this final step, we'll create a general-purpose function that can read CSV files and create objects of any class that implements the `from_row()` class method. This demonstrates the power of using class methods as a uniform interface.

## Modifying the read_portfolio() Function

First, let's update the `read_portfolio()` function in `stock.py` to use our new `from_row()` class method. Open `stock.py` and modify the `read_portfolio()` function as follows:

```python
def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of Stock instances
    '''
    import csv
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip header
        for row in rows:
            portfolio.append(Stock.from_row(row))
    return portfolio
```

This version is simpler and delegates the type conversion responsibility to the `Stock` class where it belongs.

## Creating a General-Purpose CSV Reader

Now, let's create a more general-purpose function in the `reader.py` file that can read CSV data into instances of any class that provides a `from_row()` class method.

Open `reader.py` and add the following function:

```python
def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances of the given class.

    Args:
        filename: Name of the CSV file
        cls: Class to instantiate (must have from_row class method)

    Returns:
        List of class instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip header
        for row in rows:
            records.append(cls.from_row(row))
    return records
```

This function takes a filename and a class as input, and returns a list of instances of that class created from the CSV data.

## Testing the General-Purpose CSV Reader

Let's create a test file to see our general-purpose reader in action. Create a file called `test_csv_reader.py` with the following content:

```python
# test_csv_reader.py
from reader import read_csv_as_instances
from stock import Stock
from decimal_stock import DStock

# Read portfolio as Stock instances
portfolio = read_csv_as_instances('portfolio.csv', Stock)
print(f"Portfolio contains {len(portfolio)} stocks")
print(f"First stock: {portfolio[0].name}, {portfolio[0].shares} shares at ${portfolio[0].price}")

# Read portfolio as DStock instances (with Decimal prices)
decimal_portfolio = read_csv_as_instances('portfolio.csv', DStock)
print(f"\nDecimal portfolio contains {len(decimal_portfolio)} stocks")
print(f"First stock: {decimal_portfolio[0].name}, {decimal_portfolio[0].shares} shares at ${decimal_portfolio[0].price}")

# Define a new class for reading the bus data
class BusRide:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

    @classmethod
    def from_row(cls, row):
        return cls(row[0], row[1], row[2], int(row[3]))

# Read some bus data (just the first 5 records for brevity)
print("\nReading bus data...")
import csv
with open('ctabus.csv') as f:
    rows = csv.reader(f)
    headers = next(rows)  # Skip header
    bus_rides = []
    for i, row in enumerate(rows):
        if i >= 5:  # Only read 5 records for the example
            break
        bus_rides.append(BusRide.from_row(row))

# Display the bus data
for ride in bus_rides:
    print(f"Route: {ride.route}, Date: {ride.date}, Type: {ride.daytype}, Rides: {ride.rides}")
```

Run this file to see the results:

```bash
cd ~/project
python test_csv_reader.py
```

You should see output that shows portfolio data loaded as both `Stock` and `DStock` instances, and bus route data loaded as `BusRide` instances.

## Key Benefits of This Approach

This approach demonstrates several powerful concepts:

1. **Separation of concerns**: Reading data is separate from instantiating objects.
2. **Polymorphism**: The same code works with different classes that follow the same interface.
3. **Flexibility**: We can easily change how data is converted by using different classes.
4. **Extensibility**: We can add new classes that work with our reader without changing the reader code.

This is a common pattern in Python that makes code more modular, reusable, and maintainable.

## Final Notes on Class Methods

Class methods are commonly used for alternative constructors in Python. You can often identify them by the word "from" in their name. For example:

```python
# Some examples from Python's built-in types
dict.fromkeys(['a', 'b', 'c'], 0)  # Create a dict with default values
datetime.datetime.fromtimestamp(1627776000)  # Create datetime from timestamp
int.from_bytes(b'\x00\x01', byteorder='big')  # Create int from bytes
```

By following this convention, you make your code more readable and consistent with Python's built-in libraries.
