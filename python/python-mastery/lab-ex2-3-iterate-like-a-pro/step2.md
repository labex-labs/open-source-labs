# Basic Iteration and Unpacking

The `for` statement iterates over any sequence of data. For example:

```python
>>> for row in rows:
        print(row)

['AA', '100', '32.20']
['IBM', '50', '91.10']
['CAT', '150', '83.44']
['MSFT', '200', '51.23']
['GE', '95', '40.37']
['MSFT', '50', '65.10']
['IBM', '100', '70.44']
>>>
```

Unpack the values into separate variables if you need to:

```python
>>> for name, shares, price in rows:
        print(name, shares, price)

AA 100 32.20
IBM 50 91.10
CAT 150 83.44
MSFT 200 51.23
GE 95 40.37
MSFT 50 65.10
IBM 100 70.44
>>>
```

It's somewhat common to use `_` or `__` as a throw-away variable if you don't care
about one or more of the values. For example:

```python
>>> for name, _, price in rows:
        print(name, price)

AA 32.20
IBM 91.10
CAT 83.44
MSFT 51.23
GE 40.37
MSFT 65.10
IBM 70.44
>>>
```

If you don't know how many values are being unpacked, you can use `*` as a wildcard.
Try this experiment in grouping the data by name:

```python
>>> from collections import defaultdict
>>> byname = defaultdict(list)
>>> for name, *data in rows:
        byname[name].append(data)

>>> byname['IBM']
[['50', '91.10'], ['100', '70.44']]
>>> byname['CAT']
[['150', '83.44']]
>>> for shares, price in byname['IBM']:
        print(shares, price)

50 91.10
100 70.44
>>>
```
