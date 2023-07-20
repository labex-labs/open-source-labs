# Printing a Table

Table the data read in part (b) and use it to make a nicely formatted
table. For example:

```python
>>> portfolio = read_portfolio('Data/portfolio.csv')
>>> for s in portfolio:
           print('%10s %10d %10.2f' % (s.name, s.shares, s.price))

        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
>>>
```

Take this code and put it in a function `print_portfolio()` that
produces the same output, but additionally adds some table headers.
For example:

```python
>>> portfolio = read_portfolio('Data/portfolio.csv')
>>> print_portfolio(portfolio)
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
>>>
```