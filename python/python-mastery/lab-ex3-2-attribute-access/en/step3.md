# Table Output

In Exercise 3.1, you wrote a function `print_portfolio()` that made a nicely formatted table. That function was custom tailored to a list of `Stock` objects. However, it can be completely generalized to work with any list of objects using the technique in part (b).

Create a new module called `tableformat.py`. In that program, write a function `print_table()` that takes a sequence (list) of objects, a list of attribute names, and prints a nicely formatted table. For example:

```python
>>> import stock
>>> import tableformat
>>> portfolio = stock.read_portfolio('portfolio.csv')
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

>>> tableformat.print_table(portfolio,['shares','name'])
    shares       name
---------- ----------
       100         AA
        50        IBM
       150        CAT
       200       MSFT
        95         GE
        50       MSFT
       100        IBM
>>>
```

For simplicity, just have the `print_table()` function print each field in a 10-character wide column.
