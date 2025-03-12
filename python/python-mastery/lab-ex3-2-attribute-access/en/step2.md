# Using getattr() for Generic Object Processing

The `getattr()` function is a powerful tool in Python that allows you to access attributes of an object in a dynamic way. This is particularly useful when you want to process objects in a generic manner. Instead of writing code that is specific to a particular object type, you can use `getattr()` to work with any object that has the required attributes. This flexibility makes your code more reusable and adaptable.

## Processing Multiple Attributes

Let's start by learning how to access multiple attributes of an object using the `getattr()` function. This is a common scenario when you need to extract specific information from an object.

First, open a Python interactive shell if you closed the previous one. You can do this by running the following command in your terminal:

```python
# Open a Python interactive shell if you closed the previous one
python3
```

Next, we'll import the `Stock` class and create a `Stock` object. The `Stock` class represents a stock with attributes like `name`, `shares`, and `price`.

```python
# Import the Stock class and create a stock object
from stock import Stock
s = Stock('GOOG', 100, 490.1)
```

Now, we'll define a list of attribute names that we want to access. This list will help us iterate over the attributes and print their values.

```python
# Define a list of attribute names
fields = ['name', 'shares', 'price']
```

Finally, we'll use a `for` loop to iterate over the list of attribute names and access each attribute using `getattr()`. We'll print the attribute name and its value for each iteration.

```python
# Access each attribute using getattr()
for name in fields:
    print(f"{name}: {getattr(s, 'name')}" if name == 'name' else f"{name}: {getattr(s, name)}")
```

When you run this code, you'll see the following output:

```
name: GOOG
shares: 100
price: 490.1
```

This output shows that we were able to access and print the values of multiple attributes of the `Stock` object using the `getattr()` function.

## Default Values with getattr()

The `getattr()` function also provides a useful feature: the ability to specify a default value if the attribute you're trying to access doesn't exist. This can prevent your code from raising an `AttributeError` and make it more robust.

Let's see how this works. First, we'll try to access an attribute that doesn't exist in the `Stock` object. We'll use `getattr()` and provide a default value of `'N/A'`.

```python
# Try to access an attribute that doesn't exist
print(getattr(s, 'symbol', 'N/A'))  # Output: 'N/A'
```

In this case, since the `symbol` attribute doesn't exist in the `Stock` object, `getattr()` returns the default value `'N/A'`.

Now, let's compare this with accessing an existing attribute. We'll access the `name` attribute, which does exist in the `Stock` object.

```python
# Compare with an existing attribute
print(getattr(s, 'name', 'N/A'))    # Output: 'GOOG'
```

Here, `getattr()` returns the actual value of the `name` attribute, which is `'GOOG'`.

## Processing a Collection of Objects

The `getattr()` function becomes even more powerful when you need to process a collection of objects. Let's see how we can use it to process a portfolio of stocks.

First, we'll import the `read_portfolio` function from the `stock` module. This function reads a portfolio of stocks from a CSV file and returns a list of `Stock` objects.

```python
# Import the portfolio reading function
from stock import read_portfolio
```

Next, we'll use the `read_portfolio` function to read the portfolio from a CSV file named `portfolio.csv`.

```python
# Read the portfolio from CSV file
portfolio = read_portfolio('portfolio.csv')
```

Finally, we'll use a `for` loop to iterate over the list of `Stock` objects in the portfolio. For each stock, we'll use `getattr()` to access the `name` and `shares` attributes and print their values.

```python
# Print the name and shares of each stock
for stock in portfolio:
    print(f"Stock: {getattr(stock, 'name')}, Shares: {getattr(stock, 'shares')}")
```

This approach makes your code more flexible because you can work with attribute names as strings. These strings can be passed as arguments or stored in data structures, allowing you to easily change the attributes you want to access without modifying the core logic of your code.
