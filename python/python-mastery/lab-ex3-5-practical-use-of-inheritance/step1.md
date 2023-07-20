# Preparation

One major use of classes in Python is in writing code that be
extended/adapted in various ways. To illustrate, in
[Exercise 3.2](ex3_2.md) you created a function `print_table()`
that made tables. You used this to make output from the `portfolio`
list. For example:

```python
>>> import stock
>>> import reader
>>> import tableformat
>>> portfolio = reader.read_csv_as_instances('Data/portfolio.csv', stock.Stock)
>>> tableformat.print_table(portfolio, ['name','shares','price'])
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
>>>
```

Suppose you wanted the `print_table()` function to be able to
make tables in any number of output formats such as CSV, XML, HTML,
Excel, etc. Trying to modify the function to support all of those
output formats at once would be painful. A better way to do this
involves moving the output-related formatting code to a class and using
inheritance to implement different output formats.
