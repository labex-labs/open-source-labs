# Why dictionaries?

Dictionaries are useful when there are _many_ different values and those values might be modified or manipulated. Dictionaries make your code more readable.

```python
s['price']
# vs
s[2]
```

In the last few exercises, you wrote a program that read a datafile `portfolio.csv`. Using the `csv` module, it is easy to read the file row-by-row.

```python
>>> import csv
>>> f = open('portfolio.csv')
>>> rows = csv.reader(f)
>>> next(rows)
['name', 'shares', 'price']
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>>
```

Although reading the file is easy, you often want to do more with the data than read it. For instance, perhaps you want to store it and start performing some calculations on it. Unfortunately, a raw "row" of data doesn't give you enough to work with. For example, even a simple math calculation doesn't work:

```python
>>> row = ['AA', '100', '32.20']
>>> cost = row[1] * row[2]
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>>
```

To do more, you typically want to interpret the raw data in some way and turn it into a more useful kind of object so that you can work with it later. Two simple options are tuples or dictionaries.
