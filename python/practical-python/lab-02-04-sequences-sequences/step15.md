# Exercise 2.16: Using the zip() function

In the file `portfolio.csv`, the first line contains column headers. In all previous code, we've been discarding them.

```python
>>> f = open('/home/labex/project/portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['name', 'shares', 'price']
>>>
```

However, what if you could use the headers for something useful? This is where the `zip()` function enters the picture. First try this to pair the file headers with a row of data:

```python
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>> list(zip(headers, row))
[ ('name', 'AA'), ('shares', '100'), ('price', '32.20') ]
>>>
```

Notice how `zip()` paired the column headers with the column values. We've used `list()` here to turn the result into a list so that you can see it. Normally, `zip()` creates an iterator that must be consumed by a for-loop.

This pairing is an intermediate step to building a dictionary. Now try this:

```python
>>> record = dict(zip(headers, row))
>>> record
{'price': '32.20', 'name': 'AA', 'shares': '100'}
>>>
```

This transformation is one of the most useful tricks to know about when processing a lot of data files. For example, suppose you wanted to make the `pcost.py` program work with various input files, but without regard for the actual column number where the name, shares, and price appear.

Modify the `portfolio_cost()` function in `pcost.py` so that it looks like this:

```python
# pcost.py

def portfolio_cost(filename):
    ...
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            # This catches errors in int() and float() conversions above
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
        ...
```

Now, try your function on a completely different data file `portfoliodate.csv` which looks like this:

```csv
name,date,time,shares,price
"AA","6/11/2007","9:50am",100,32.20
"IBM","5/13/2007","4:20pm",50,91.10
"CAT","9/23/2006","1:30pm",150,83.44
"MSFT","5/17/2007","10:30am",200,51.23
"GE","2/1/2006","10:45am",95,40.37
"MSFT","10/31/2006","12:05pm",50,65.10
"IBM","7/9/2006","3:15pm",100,70.44
```

```python
>>> portfolio_cost('/home/labex/project/portfoliodate.csv')
44671.15
>>>
```

If you did it right, you'll find that your program still works even though the data file has a completely different column format than before. That's cool!

The change made here is subtle, but significant. Instead of `portfolio_cost()` being hardcoded to read a single fixed file format, the new version reads any CSV file and picks the values of interest out of it. As long as the file has the required columns, the code will work.

Modify the `report.py` program you wrote in Section 2.3 so that it uses the same technique to pick out column headers.

Try running the `report.py` program on the `portfoliodate.csv` file and see that it produces the same answer as before.

```python
import csv

def portfolio_cost(filename):
    total_cost = 0
    with open(filename, 'r') as file:
        rows = csv.reader(file)
        headers = next(rows)  # Get the column headers
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))  # Pair column headers with row data
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
    return total_cost

cost = portfolio_cost('/home/labex/project/portfoliodate.csv')
print(cost)
```
