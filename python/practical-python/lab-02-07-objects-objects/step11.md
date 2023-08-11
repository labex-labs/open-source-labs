# Exercise 2.24: First-class Data

In the file `portfolio.csv`, we read data organized as columns that look like this:

```csv
name,shares,price
"AA",100,32.20
"IBM",50,91.10
...
```

In previous code, we used the `csv` module to read the file, but still had to perform manual type conversions. For example:

```python
for row in rows:
    name   = row[0]
    shares = int(row[1])
    price  = float(row[2])
```

This kind of conversion can also be performed in a more clever manner using some list basic operations.

Make a Python list that contains the names of the conversion functions you would use to convert each column into the appropriate type:

```python
>>> types = [str, int, float]
>>>
```

The reason you can even create this list is that everything in Python is _first-class_. So, if you want to have a list of functions, that's fine. The items in the list you created are functions for converting a value `x` into a given type (e.g., `str(x)`, `int(x)`, `float(x)`).

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

As noted, this row isn't enough to do calculations because the types are wrong. For example:

```python
>>> row[1] * row[2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>>
```

However, maybe the data can be paired up with the types you specified in `types`. For example:

```python
>>> types[1]
<type 'int'>
>>> row[1]
'100'
>>>
```

Try converting one of the values:

```python
>>> types[1](row[1])     # Same as int(row[1])
100
>>>
```

Try converting a different value:

```python
>>> types[2](row[2])     # Same as float(row[2])
32.2
>>>
```

Try the calculation with converted values:

```python
>>> types[1](row[1])*types[2](row[2])
3220.0000000000005
>>>
```

Zip the column types with the fields and look at the result:

```python
>>> r = list(zip(types, row))
>>> r
[(<type 'str'>, 'AA'), (<type 'int'>, '100'), (<type 'float'>,'32.20')]
>>>
```

You will notice that this has paired a type conversion with a value. For example, `int` is paired with the value `'100'`.

The zipped list is useful if you want to perform conversions on all of the values, one after the other. Try this:

```python
>>> converted = []
>>> for func, val in zip(types, row):
          converted.append(func(val))
...
>>> converted
['AA', 100, 32.2]
>>> converted[1] * converted[2]
3220.0000000000005
>>>
```

Make sure you understand what's happening in the above code. In the loop, the `func` variable is one of the type conversion functions (e.g., `str`, `int`, etc.) and the `val` variable is one of the values like `'AA'`, `'100'`. The expression `func(val)` is converting a value (kind of like a type cast).

The above code can be compressed into a single list comprehension.

```python
>>> converted = [func(val) for func, val in zip(types, row)]
>>> converted
['AA', 100, 32.2]
>>>
```
