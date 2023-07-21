# Exercise 2.23: Extracting Data From CSV Files

Knowing how to use various combinations of list, set, and dictionary
comprehensions can be useful in various forms of data processing.
Here’s an example that shows how to extract selected columns from a
CSV file.

First, read a row of header information from a CSV file:

```python
>>> import csv
>>> f = open('Data/portfoliodate.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['name', 'date', 'time', 'shares', 'price']
>>>
```

Next, define a variable that lists the columns that you actually care about:

```python
>>> select = ['name', 'shares', 'price']
>>>
```

Now, locate the indices of the above columns in the source CSV file:

```python
>>> indices = [ headers.index(colname) for colname in select ]
>>> indices
[0, 3, 4]
>>>
```

Finally, read a row of data and turn it into a dictionary using a
dictionary comprehension:

```python
>>> row = next(rows)
>>> record = { colname: row[index] for colname, index in zip(select, indices) }   # dict-comprehension
>>> record
{'price': '32.20', 'name': 'AA', 'shares': '100'}
>>>
```

If you’re feeling comfortable with what just happened, read the rest
of the file:

```python
>>> portfolio = [ { colname: row[index] for colname, index in zip(select, indices) } for row in rows ]
>>> portfolio
[{'price': '91.10', 'name': 'IBM', 'shares': '50'}, {'price': '83.44', 'name': 'CAT', 'shares': '150'},
  {'price': '51.23', 'name': 'MSFT', 'shares': '200'}, {'price': '40.37', 'name': 'GE', 'shares': '95'},
  {'price': '65.10', 'name': 'MSFT', 'shares': '50'}, {'price': '70.44', 'name': 'IBM', 'shares': '100'}]
>>>
```

Oh my, you just reduced much of the `read_portfolio()` function to a single statement.
