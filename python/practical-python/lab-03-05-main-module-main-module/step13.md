# Exercise 3.15: `main()` functions

In the file `report.py` add a `main()` function that accepts a list of
command line options and produces the same output as before. You
should be able to run it interactively like this:

```python
>>> import report
>>> report.main(['report.py', 'Data/portfolio.csv', 'Data/prices.csv'])
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

Modify the `pcost.py` file so that it has a similar `main()` function:

```python
>>> import pcost
>>> pcost.main(['pcost.py', 'Data/portfolio.csv'])
Total cost: 44671.15
>>>
```
