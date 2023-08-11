# Exercise 6.10: Making more pipeline components

Let's extend the whole idea into a larger pipeline. In a separate file `ticker.py`, start by creating a function that reads a CSV file as you did above:

```python
# ticker.py

from follow import follow
import csv

def parse_stock_data(lines):
    rows = csv.reader(lines)
    return rows

if __name__ == '__main__':
    lines = follow('stocklog.csv')
    rows = parse_stock_data(lines)
    for row in rows:
        print(row)
```

Write a new function that selects specific columns:

    # ticker.py
    ...
    def select_columns(rows, indices):
        for row in rows:
            yield [row[index] for index in indices]
    ...
    def parse_stock_data(lines):
        rows = csv.reader(lines)
        rows = select_columns(rows, [0, 1, 4])
        return rows

Run your program again. You should see output narrowed down like this:

    ['BA', '98.35', '0.16']
    ['AA', '39.63', '-0.03']
    ['XOM', '82.45','-0.23']
    ['PG', '62.95', '-0.12']
    ...

Write generator functions that convert data types and build dictionaries. For example:

```python
# ticker.py
...

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))
...
def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows
...
```

Run your program again. You should now a stream of dictionaries like this:

    { 'name':'BA', 'price':98.35, 'change':0.16 }
    { 'name':'AA', 'price':39.63, 'change':-0.03 }
    { 'name':'XOM', 'price':82.45, 'change': -0.23 }
    { 'name':'PG', 'price':62.95, 'change':-0.12 }
    ...
