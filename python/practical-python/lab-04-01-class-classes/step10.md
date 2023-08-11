# Exercise 4.4: Using your class

Modify the `read_portfolio()` function in the `report.py` program so that it reads a portfolio into a list of `Stock` instances as just shown in Exercise 4.3. Once you have done that, fix all of the code in `report.py` and `pcost.py` so that it works with `Stock` instances instead of dictionaries.

Hint: You should not have to make major changes to the code. You will mainly be changing dictionary access such as `s['shares']` into `s.shares`.

You should be able to run your functions the same as before:

```python
>>> import pcost
>>> pcost.portfolio_cost('portfolio.csv')
44671.15
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84
>>>
```
