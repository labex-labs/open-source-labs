# Exercise 2.15: A practical enumerate() example

Recall that the file `missing.csv` contains data for a stock portfolio, but has some rows with missing data. Using `enumerate()`, modify your `pcost.py` program so that it prints a line number with the warning message when it encounters bad input.

```python
>>> cost = portfolio_cost('/home/labex/project/missing.csv')
Row 4: Couldn't convert: ['MSFT', '', '51.23']
Row 7: Couldn't convert: ['IBM', '', '70.44']
>>>
```

To do this, you'll need to change a few parts of your code.

```python
...
for rowno, row in enumerate(rows, start=1):
    try:
        ...
    except ValueError:
        print(f'Row {rowno}: Bad row: {row}')
```

Here's a solution:

```python
import csv

def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'r') as file:
        rows = csv.reader(file)
        for rowno, row in enumerate(rows, start=1):
            try:
                shares = int(row[1])
                price = float(row[2])
                cost = shares * price
                total_cost += cost
            except ValueError:
                print(f'Row {rowno}: Couldn\'t convert: {row}')
    return total_cost

cost = portfolio_cost('/home/labex/project/missing.csv')
print(cost)
```