# Exercise 3.12: Using your library module

In section 2, you wrote a program `report.py` that produced a stock report like this:

```
      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84
```

Take that program and modify it so that all of the input file
processing is done using functions in your `fileparse` module. To do
that, import `fileparse` as a module and change the `read_portfolio()`
and `read_prices()` functions to use the `parse_csv()` function.

Use the interactive example at the start of this exercise as a guide.
Afterwards, you should get exactly the same output as before.
