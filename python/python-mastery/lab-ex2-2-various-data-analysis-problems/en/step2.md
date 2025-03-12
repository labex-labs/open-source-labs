# Using List, Set, and Dictionary Comprehensions

Python comprehensions are a concise way to create new collections from existing ones. They can help you filter, transform, and organize data efficiently. Let's explore them using our portfolio data.

Open a Python terminal as you did in the previous step and enter the following examples one by one:

## List Comprehensions

A list comprehension creates a new list by applying an expression to each item in an existing collection:

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')

# Find all holdings with more than 100 shares
>>> large_holdings = [s for s in portfolio if s['shares'] > 100]
>>> print(large_holdings)
[{'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'MSFT', 'shares': 200, 'price': 51.23}]
```

This code creates a new list containing only the holdings where the number of shares is greater than 100.

You can also use list comprehensions to perform calculations:

```python
# Calculate the total cost of each holding (shares * price)
>>> holding_costs = [s['shares'] * s['price'] for s in portfolio]
>>> print(holding_costs)
[3220.0, 4555.0, 12516.0, 10246.0, 3835.15, 3255.0, 7044.0]

# Calculate the total cost of the entire portfolio
>>> total_portfolio_cost = sum([s['shares'] * s['price'] for s in portfolio])
>>> print(total_portfolio_cost)
44671.15
```

## Set Comprehensions

A set comprehension creates a set (a collection of unique values) from an existing collection:

```python
# Find all unique stock names
>>> unique_stocks = {s['name'] for s in portfolio}
>>> print(unique_stocks)
{'MSFT', 'IBM', 'AA', 'GE', 'CAT'}
```

Since sets only contain unique values, this gives us a list of all the different stocks in our portfolio without duplicates.

## Dictionary Comprehensions

A dictionary comprehension creates a new dictionary by applying expressions to create key-value pairs:

```python
# Create a dictionary to count total shares for each stock
>>> totals = {s['name']: 0 for s in portfolio}
>>> for s in portfolio:
...     totals[s['name']] += s['shares']
...
>>> print(totals)
{'AA': 100, 'IBM': 150, 'CAT': 150, 'MSFT': 250, 'GE': 95}
```

This code first creates a dictionary with each stock name as a key and 0 as the initial value. Then, it loops through the portfolio and adds up the shares for each stock.

These comprehensions provide a powerful way to transform and analyze data with minimal code.
