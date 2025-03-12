# Using getattr() for Generic Object Processing

The `getattr()` function is particularly useful for processing objects in a generic way. This allows you to write code that works with any object type, as long as it has the required attributes.

## Processing Multiple Attributes

Let's see how to access multiple attributes of an object using `getattr()`:

```python
# Open a Python interactive shell if you closed the previous one
python3

# Import the Stock class and create a stock object
from stock import Stock
s = Stock('GOOG', 100, 490.1)

# Define a list of attribute names
fields = ['name', 'shares', 'price']

# Access each attribute using getattr()
for name in fields:
    print(f"{name}: {getattr(s, 'name')}" if name == 'name' else f"{name}: {getattr(s, name)}")
```

Output:

```
name: GOOG
shares: 100
price: 490.1
```

## Default Values with getattr()

The `getattr()` function also allows you to provide a default value if an attribute doesn't exist:

```python
# Try to access an attribute that doesn't exist
print(getattr(s, 'symbol', 'N/A'))  # Output: 'N/A'

# Compare with an existing attribute
print(getattr(s, 'name', 'N/A'))    # Output: 'GOOG'
```

## Processing a Collection of Objects

Let's see how we can process a collection of objects using `getattr()`:

```python
# Import the portfolio reading function
from stock import read_portfolio

# Read the portfolio from CSV file
portfolio = read_portfolio('portfolio.csv')

# Print the name and shares of each stock
for stock in portfolio:
    print(f"Stock: {getattr(stock, 'name')}, Shares: {getattr(stock, 'shares')}")
```

This approach makes your code more flexible because you can work with attribute names as strings, which can be passed as arguments or stored in data structures.
