# Creating a General-Purpose CSV Reader

In this final step, we're going to create a general-purpose function. This function will be able to read CSV files and create objects of any class that has implemented the `from_row()` class method. This shows us the power of using class methods as a uniform interface. A uniform interface means that different classes can be used in the same way, which makes our code more flexible and easier to manage.

## Modifying the read_portfolio() Function

First, we'll update the `read_portfolio()` function in the `stock.py` file. We'll use our new `from_row()` class method. Open the `stock.py` file and change the `read_portfolio()` function like this:

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

This new version of the function is simpler. It gives the responsibility of type conversion to the `Stock` class, where it really belongs. Type conversion means changing the data from one type to another, like turning a string into an integer. By doing this, we make our code more organized and easier to understand.

## Creating a General-Purpose CSV Reader

Now, we'll create a more general-purpose function in the `reader.py` file. This function can read CSV data and create instances of any class that has a `from_row()` class method.

Open the `reader.py` file and add the following function:

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

This function takes two inputs: a filename and a class. It then returns a list of instances of that class, created from the data in the CSV file. This is very useful because we can use it with different classes, as long as they have the `from_row()` method.

## Testing the General-Purpose CSV Reader

Let's create a test file to see how our general-purpose reader works. Create a file named `test_csv_reader.py` with the following content:

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

Run this file to see the results. Open your terminal and use the following commands:

```bash
cd ~/project
python test_csv_reader.py
```

You should see output that shows the portfolio data loaded as both `Stock` and `DStock` instances, and the bus route data loaded as `BusRide` instances. This proves that our general-purpose reader works with different classes.

## Key Benefits of This Approach

This approach shows several powerful concepts:

1. **Separation of concerns**: Reading data is separate from creating objects. This means that the code for reading the CSV file is not mixed with the code for creating objects. It makes the code easier to understand and maintain.
2. **Polymorphism**: The same code can work with different classes that follow the same interface. In our case, as long as a class has the `from_row()` method, our general-purpose reader can use it.
3. **Flexibility**: We can easily change how data is converted by using different classes. For example, we can use `Stock` or `DStock` to handle the portfolio data differently.
4. **Extensibility**: We can add new classes that work with our reader without changing the reader code. This makes our code more future-proof.

This is a common pattern in Python that makes code more modular, reusable, and maintainable.

## Final Notes on Class Methods

Class methods are often used as alternative constructors in Python. You can usually tell them apart because their names often have the word "from" in them. For example:

```python
# Some examples from Python's built-in types
dict.fromkeys(['a', 'b', 'c'], 0)  # Create a dict with default values
datetime.datetime.fromtimestamp(1627776000)  # Create datetime from timestamp
int.from_bytes(b'\x00\x01', byteorder='big')  # Create int from bytes
```

By following this convention, you make your code more readable and consistent with Python's built-in libraries. This helps other developers understand your code more easily.
