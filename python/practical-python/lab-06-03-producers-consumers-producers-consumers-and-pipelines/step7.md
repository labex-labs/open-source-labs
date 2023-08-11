# Exercise 6.12: Putting it all together

In the `ticker.py` program, write a function `ticker(portfile, logfile, fmt)` that creates a real-time stock ticker from a given portfolio, logfile, and table format. For example::

```python
>>> from ticker import ticker
>>> ticker('portfolio.csv', 'stocklog.csv', 'txt')
      Name      Price     Change
---------- ---------- ----------
        GE      37.14      -0.18
      MSFT      29.96      -0.09
       CAT      78.03      -0.49
        AA      39.34      -0.32
...

>>> ticker('portfolio.csv', 'stocklog.csv', 'csv')
Name,Price,Change
IBM,102.79,-0.28
CAT,78.04,-0.48
AA,39.35,-0.31
CAT,78.05,-0.47
...
```
