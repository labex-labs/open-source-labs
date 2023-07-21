# Exercise 2.4: A list of tuples

The file `Data/portfolio.csv` contains a list of stocks in a
portfolio. In [Exercise 1.30](../01_Introduction/07_Functions.md), you
wrote a function `portfolio_cost(filename)` that read this file and
performed a simple calculation.

Your code should have looked something like this:

```python
# pcost.py

import csv

def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost
```

Using this code as a rough guide, create a new file `report.py`. In
that file, define a function `read_portfolio(filename)` that opens a
given portfolio file and reads it into a list of tuples. To do this,
you’re going to make a few minor modifications to the above code.

First, instead of defining `total_cost = 0`, you’ll make a variable
that’s initially set to an empty list. For example:

```python
portfolio = []
```

Next, instead of totaling up the cost, you’ll turn each row into a
tuple exactly as you just did in the last exercise and append it to
this list. For example:

```python
for row in rows:
    holding = (row[0], int(row[1]), float(row[2]))
    portfolio.append(holding)
```

Finally, you’ll return the resulting `portfolio` list.

Experiment with your function interactively (just a reminder that in
order to do this, you first have to run the `report.py` program in the
interpreter):

_Hint: Use `-i` when executing the file in the terminal_

```python
>>> portfolio = read_portfolio('Data/portfolio.csv')
>>> portfolio
[('AA', 100, 32.2), ('IBM', 50, 91.1), ('CAT', 150, 83.44), ('MSFT', 200, 51.23),
    ('GE', 95, 40.37), ('MSFT', 50, 65.1), ('IBM', 100, 70.44)]
>>>
>>> portfolio[0]
('AA', 100, 32.2)
>>> portfolio[1]
('IBM', 50, 91.1)
>>> portfolio[1][1]
50
>>> total = 0.0
>>> for s in portfolio:
        total += s[1] * s[2]

>>> print(total)
44671.15
>>>
```

This list of tuples that you have created is very similar to a 2-D
array. For example, you can access a specific column and row using a
lookup such as `portfolio[row][column]` where `row` and `column` are
integers.

That said, you can also rewrite the last for-loop using a statement like this:

```python
>>> total = 0.0
>>> for name, shares, price in portfolio:
            total += shares*price

>>> print(total)
44671.15
>>>
```
