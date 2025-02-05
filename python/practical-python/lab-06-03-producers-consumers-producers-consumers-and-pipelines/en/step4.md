# Exercise 6.9: Setting up a more complex pipeline

Take the pipelining idea a few steps further by performing more actions.

```python
>>> from follow import follow
>>> import csv
>>> lines = follow('stocklog.csv')
>>> rows = csv.reader(lines)
>>> for row in rows:
        print(row)

['GOOG', '1502.08', '2023-10-01', '09:37.19', '1.83', '1500.25', '1502.08', '1500.25', '731']
['AAPL', '252.33', '2023-10-01', '09:37.19', '1.83', '250.50', '252.33', '250.50', '681']
['GOOG', '1502.09', '2023-10-01', '09:37.21', '1.84', '1500.25', '1502.09', '1500.25', '734']
['AAPL', '252.34', '2023-10-01', '09:37.21', '1.84', '250.50', '252.34', '250.50', '684']
['GOOG', '1502.10', '2023-10-01', '09:37.23', '1.85', '1500.25', '1502.10', '1500.25', '738']
['AAPL', '252.35', '2023-10-01', '09:37.23', '1.85', '250.50', '252.35', '250.50', '688']
...
```

Well, that's interesting. What you're seeing here is that the output of the `follow()` function has been piped into the `csv.reader()` function and we're now getting a sequence of split rows.
