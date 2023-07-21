# Exercise 4.8: Putting it all together

Modify the `report.py` program so that the `portfolio_report()` function takes
an optional argument specifying the output format. For example:

```python
>>> report.portfolio_report('Data/portfolio.csv', 'Data/prices.csv', 'txt')
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

Modify the main program so that a format can be given on the command line:

```bash
bash $ python3 report.py Data/portfolio.csv Data/prices.csv csv
Name,Shares,Price,Change
AA,100,9.22,-22.98
IBM,50,106.28,15.18
CAT,150,35.46,-47.98
MSFT,200,20.89,-30.34
GE,95,13.48,-26.89
MSFT,50,20.89,-44.21
IBM,100,106.28,35.84
bash $
```
