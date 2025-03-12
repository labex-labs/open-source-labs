# Exploring the Collections Module

In Python, the built - in containers such as lists, dictionaries, and sets are very useful. However, Python's `collections` module takes it a step further by providing specialized container datatypes that extend the functionality of these built - in containers. Let's take a closer look at some of these useful datatypes.

You'll continue working in your Python terminal and follow along with the examples below.

## Counter

The `Counter` class is a subclass of the dictionary. Its main purpose is to count hashable objects. It offers a convenient way to count items and supports a variety of operations.

First, we need to import the `Counter` class and a function to read a portfolio. Then we'll read a portfolio from a CSV file.

```python
>>> from collections import Counter
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')

```

Now, we'll create a `Counter` object to count the number of shares for each stock by its name.

```python
# Create a counter to count shares by stock name
>>> totals = Counter()
>>> for s in portfolio:
...     totals[s['name']] += s['shares']
...
>>> print(totals)
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
```

One of the great features of the `Counter` object is that it automatically initializes new keys with a count of 0. This means you don't have to check if a key exists before incrementing its count, which simplifies the code for accumulating counts.

Counters also come with special methods. For example, the `most_common()` method is very useful for data analysis.

```python
# Get the two stocks with the most shares
>>> most_common_stocks = totals.most_common(2)
>>> print(most_common_stocks)
[('MSFT', 250), ('IBM', 150)]
```

In addition, counters can be combined using arithmetic operations.

```python
# Create another counter
>>> more = Counter()
>>> more['IBM'] = 75
>>> more['AA'] = 200
>>> more['ACME'] = 30
>>> print(more)
Counter({'AA': 200, 'IBM': 75, 'ACME': 30})

# Add two counters together
>>> combined = totals + more
>>> print(combined)
Counter({'AA': 300, 'MSFT': 250, 'IBM': 225, 'CAT': 150, 'GE': 95, 'ACME': 30})
```

## defaultdict

The `defaultdict` is similar to a regular dictionary, but it has a unique feature. It provides a default value for keys that don't exist yet. This can simplify your code, as you no longer need to check if a key exists before using it.

```python
>>> from collections import defaultdict

# Group portfolio entries by stock name
>>> byname = defaultdict(list)
>>> for s in portfolio:
...     byname[s['name']].append(s)
...
>>> print(byname['IBM'])
[{'name': 'IBM', 'shares': 50, 'price': 91.1}, {'name': 'IBM', 'shares': 100, 'price': 70.44}]
>>> print(byname['AA'])
[{'name': 'AA', 'shares': 100, 'price': 32.2}]
```

When you create a `defaultdict(list)`, it automatically creates a new empty list for each new key. So, you can directly append to a key's value even if the key didn't exist before. This eliminates the need to check if the key exists and create an empty list manually.

You can also use other default factory functions. For example, you can use `int`, `float`, or even your own custom function.

```python
# Use defaultdict with int to count items
>>> word_counts = defaultdict(int)
>>> words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
>>> for word in words:
...     word_counts[word] += 1
...
>>> print(word_counts)
defaultdict(<class 'int'>, {'apple': 3, 'orange': 2, 'banana': 1})
```

These specialized container types from the `collections` module can make your code more concise and efficient when you're working with data.
