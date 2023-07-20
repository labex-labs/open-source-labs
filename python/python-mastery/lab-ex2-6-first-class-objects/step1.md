# First-class Data

In the file `portfolio.csv`, you read data organized as columns
that look like this:

```python
"AA",100,32.20
"IBM",50,91.10
...
```

In previous code, this data was processed by hard-coding all of the
type conversions. For example:

```python
rows = csv.reader(f)
for row in rows:
    name   = row[0]
    shares = int(row[1])
    price  = float(row[2])
```

This kind of conversion can also be performed in a more clever manner
using some list operations. Make a Python list that contains the
conversions you want to carry out on each column:

```python
>>> coltypes = [str, int, float]
>>>
```

The reason you can even create this list is that everything in Python
is "first-class." So, if you want to have a list of functions, that's
fine.

Now, read a row of data from the above file:

```python
>>> import csv
>>> f = open('portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>>
```

Zip the column types with the row and look at the result:

```python
>>> r = list(zip(coltypes, row))
>>> r
[(<class 'str'>, 'AA'), (<class 'int'>, '100'), (<class 'float'>,'32.20')]
>>>
```

You will notice that this has paired a type conversion with a value. For example, `int` is
paired with the value `'100'`. Now, try this:

```python
>>> record = [func(val) for func, val in zip(coltypes, row)]
>>> record
['AA', 100, 32.2]
>>>
```

Make sure you understand what's happening in the above code. In the
loop, the `func` variable is one of the type conversion functions
(e.g., `str`, `int`, etc.) and the `val` variable is one of the values
like `'AA'`, `'100'`. The expression `func(val)` is converting
a value (kind of like a type cast).

You can take it a step further and make dictionaries by using the column
headers. For example:

```python
>>> dict(zip(headers, record))
{'name': 'AA', 'shares': 100, 'price': 32.2}
>>>
```

If you prefer, you can perform all of these steps at once using a
dictionary comprehension:

```python
>>> { name:func(val) for name, func, val in zip(headers, coltypes, row) }
{'name': 'AA', 'shares': 100, 'price': 32.2}
>>>
```
