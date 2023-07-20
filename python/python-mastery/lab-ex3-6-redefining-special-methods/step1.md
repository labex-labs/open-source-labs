# Better output for representing objects

All Python objects have two string representations. The first
representation is created by string conversion via `str()`
(which is called by `print`). The string representation is
usually a nicely formatted version of the object meant for humans.
The second representation is a code representation of the object
created by `repr()` (or simply by viewing a value in the
interactive shell). The code representation typically shows you the
code that you have to type to get the object. Here is an example
that illustrates using dates:

```python
>>> from datetime import date
>>> d = date(2008, 7, 5)
>>> print(d)              # uses str()
2008-07-05
>>> d    # uses repr()
datetime.date(2008, 7, 5)
>>>
```

There are several techniques for obtaining the `repr()` string
in output:

```python
>>> print('The date is', repr(d))
The date is datetime.date(2008, 7, 5)
>>> print(f'The date is {d!r}')
The date is datetime.date(2008, 7, 5)
>>> print('The date is %r' % d)
The date is datetime.date(2008, 7, 5)
>>>
```

Modify the `Stock` object that you've created so that
the `__repr__()` method
produces more useful output. For example:

```python
>>> goog = Stock('GOOG', 100, 490.10)
>>> goog
Stock('GOOG', 100, 490.1)
>>>
```

See what happens when you read a portfolio of stocks and view the
resulting list after you have made these changes. For example:

```python
>>> import stock, reader
>>> portfolio = reader.read_csv_as_instances('Data/portfolio.csv', stock.Stock)
>>> portfolio
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44), Stock('MSFT', 200, 51.23),
 Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.1), Stock('IBM', 100, 70.44)]
>>>
```
