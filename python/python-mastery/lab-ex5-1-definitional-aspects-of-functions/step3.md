# Thinking about Flexibility

Right now, the two functions in `reader.py` are hard-wired to work
with filenames that are passed directly to `open()`. Refactor the
code so that it works with any iterable object that produces lines.
To do this, create two new functions `csv_as_dicts(lines, types)` and
`csv_as_instances(lines, cls)` that convert any iterable sequence of
lines. For example:

```python
>>> file = open('Data/portfolio.csv')
>>> port = reader.csv_as_dicts(file, [str, int, float])
>>> port
[{'name': 'AA', 'shares': 100, 'price': 32.2}, {'name': 'IBM', 'shares': 50, 'price': 91.1},
 {'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'MSFT', 'shares': 200, 'price': 51.23},
 {'name': 'GE', 'shares': 95, 'price': 40.37}, {'name': 'MSFT', 'shares': 50, 'price': 65.1},
 {'name': 'IBM', 'shares': 100, 'price': 70.44}]
>>>
```

The whole point of doing this is to make it possible to work with different
kinds of input sources. For example:

```python
>>> import gzip
>>> import stock
>>> file = gzip.open('Data/portfolio.csv.gz')
>>> port = reader.csv_as_instances(file, stock.Stock)
>>> port
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44),
 Stock('MSFT', 200, 51.23), Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.1),
 Stock('IBM', 100, 70.44)]
>>>
```

To maintain backwards compatibility with older code, write functions
`read_csv_as_dicts()` and `read_csv_as_instances()` that take a
filename as before. These functions should call `open()` on the
supplied filename and use the new `csv_as_dicts()` or
`csv_as_instances()` functions on the resulting file.
