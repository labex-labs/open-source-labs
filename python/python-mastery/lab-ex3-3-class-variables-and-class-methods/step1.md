# Previous Exercise

Instances of the `Stock` class defined in the previous exercise are
normally created as follows:

```python
>>> s = Stock('GOOG', 100, 490.1)
>>>
```

However, the `read_portfolio()` function also creates instances from rows
of data read from files. For example, code such as the following is used:

```python
>>> import csv
>>> f = open('Data/portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>> s = Stock(row[0], int(row[1]), float(row[2]))
>>>
```
