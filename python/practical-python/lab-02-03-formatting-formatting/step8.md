# Exercise 2.10: Printing a formatted table

Redo the for-loop in Exercise 2.9, but change the print statement to format the tuples.

```python
>>> for r in report:
        print('%10s %10d %10.2f %10.2f' % r)

          AA        100       9.22     -22.98
         IBM         50     106.28      15.18
         CAT        150      35.46     -47.98
        MSFT        200      20.89     -30.34
...
>>>
```

You can also expand the values and use f-strings. For example:

```python
>>> for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

          AA        100       9.22     -22.98
         IBM         50     106.28      15.18
         CAT        150      35.46     -47.98
        MSFT        200      20.89     -30.34
...
>>>
```

Take the above statements and add them to your `report.py` program. Have your program take the output of the `make_report()` function and print a nicely formatted table as shown.

