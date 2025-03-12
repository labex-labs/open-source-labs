# Exploring the Collections Module

Python's `collections` module provides specialized container datatypes that extend the functionality of Python's built-in containers like lists, dictionaries, and sets. Let's explore some of these useful datatypes.

Continue in your Python terminal with the following examples:

## Counter

The `Counter` class is a dict subclass designed for counting hashable objects. It's a convenient way to count items and supports various operations:

```python
>>> from collections import Counter
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')

# Create a counter to count shares by stock name
>>> totals = Counter()
>>> for s in portfolio:
...     totals[s['name']] += s['shares']
...
>>> print(totals)
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
```

The `Counter` object automatically initializes new keys with a count of 0, making it simple to accumulate counts without checking if a key exists first.

Counters also have special methods like `most_common()` that make them useful for analysis:

```python
# Get the two stocks with the most shares
>>> most_common_stocks = totals.most_common(2)
>>> print(most_common_stocks)
[('MSFT', 250), ('IBM', 150)]
```

Counters can be combined with arithmetic operations:

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

The `defaultdict` is similar to a regular dictionary, but it provides a default value for keys that don't exist yet. This can simplify code that would otherwise require key existence checks:

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

The `defaultdict(list)` creates a new empty list automatically for each new key. This means you can append to a key's value even if that key didn't exist before - removing the need to check if the key exists and create an empty list manually.

You can use other default factory functions like `int`, `float`, or even your own custom function:

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

These specialized container types from the `collections` module can make your code more concise and efficient when working with data.
