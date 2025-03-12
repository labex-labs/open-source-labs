# Using List, Set, and Dictionary Comprehensions

Python comprehensions are a really useful and concise way to create new collections based on existing ones. Collections in Python can be lists, sets, or dictionaries, which are like containers that hold different types of data. Comprehensions allow you to filter out certain data, transform the data in some way, and organize it more efficiently. In this part, we'll use our portfolio data to explore how these comprehensions work.

First, you need to open a Python terminal, just like you did in the previous step. Once the terminal is open, you'll enter the following examples one by one. This hands - on approach will help you understand how comprehensions work in practice.

## List Comprehensions

A list comprehension is a special syntax in Python that creates a new list. It does this by applying an expression to each item in an existing collection.

Let's start with an example. First, we'll import a function to read our portfolio data. Then we'll use list comprehension to filter out certain holdings from the portfolio.

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')

# Find all holdings with more than 100 shares
>>> large_holdings = [s for s in portfolio if s['shares'] > 100]
>>> print(large_holdings)
[{'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'MSFT', 'shares': 200, 'price': 51.23}]
```

In this code, we first import the `read_portfolio` function and use it to read the portfolio data from a CSV file. Then, the list comprehension `[s for s in portfolio if s['shares'] > 100]` goes through each item `s` in the `portfolio` collection. It only includes the item `s` in the new list `large_holdings` if the number of shares in that holding is greater than 100.

List comprehensions can also be used to perform calculations. Here are some examples:

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

In the first example, the list comprehension `[s['shares'] * s['price'] for s in portfolio]` calculates the total cost of each holding by multiplying the number of shares by the price for each item in the `portfolio`. In the second example, we use the `sum` function along with the list comprehension to calculate the total cost of the entire portfolio.

## Set Comprehensions

A set comprehension is used to create a set from an existing collection. A set is a collection that only contains unique values.

Let's see how it works with our portfolio data:

```python
# Find all unique stock names
>>> unique_stocks = {s['name'] for s in portfolio}
>>> print(unique_stocks)
{'MSFT', 'IBM', 'AA', 'GE', 'CAT'}
```

In this code, the set comprehension `{s['name'] for s in portfolio}` goes through each item `s` in the `portfolio` and adds the stock name (`s['name']`) to the set `unique_stocks`. Since sets only store unique values, we end up with a list of all the different stocks in our portfolio without any duplicates.

## Dictionary Comprehensions

A dictionary comprehension creates a new dictionary by applying expressions to create key - value pairs.

Here's an example of using a dictionary comprehension to count the total number of shares for each stock in our portfolio:

```python
# Create a dictionary to count total shares for each stock
>>> totals = {s['name']: 0 for s in portfolio}
>>> for s in portfolio:
...     totals[s['name']] += s['shares']
...
>>> print(totals)
{'AA': 100, 'IBM': 150, 'CAT': 150, 'MSFT': 250, 'GE': 95}
```

In the first line, the dictionary comprehension `{s['name']: 0 for s in portfolio}` creates a dictionary where each stock name (`s['name']`) is a key, and the initial value for each key is 0. Then, we use a `for` loop to go through each item in the `portfolio`. For each item, we add the number of shares (`s['shares']`) to the corresponding value in the `totals` dictionary.

These comprehensions are very powerful because they allow you to transform and analyze data with just a few lines of code. They are a great tool to have in your Python programming toolkit.
