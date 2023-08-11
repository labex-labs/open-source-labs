# Exercise 2.15: A practical enumerate() example

Recall that the file `missing.csv` contains data for a stock portfolio, but has some rows with missing data. Using `enumerate()`, modify your `pcost.py` program so that it prints a line number with the warning message when it encounters bad input.

```python
>>> cost = portfolio_cost('missing.csv')
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
