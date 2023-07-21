# Exercise 9.3: Top-level Scripts

Using the `python -m` command is often a bit weird. You may want to
write a top level script that simply deals with the oddities of packages.
Create a script `print-report.py` that produces the above report:

```python
#!/usr/bin/env python3
# print-report.py
import sys
from porty.report import main
main(sys.argv)
```

Put this script in the top-level `porty-app/` directory. Make sure you
can run it in that location:

```
shell % cd porty-app
shell % python3 print-report.py portfolio.csv prices.csv txt
      Name     Shares      Price     Change
---------- ---------- ---------- ----------
        AA        100       9.22     -22.98
       IBM         50     106.28      15.18
       CAT        150      35.46     -47.98
      MSFT        200      20.89     -30.34
        GE         95      13.48     -26.89
      MSFT         50      20.89     -44.21
       IBM        100     106.28      35.84

shell %
```

Your final code should now be structured something like this:

```
porty-app/
    portfolio.csv
    prices.csv
    print-report.py
    README.txt
    porty/
        __init__.py
        fileparse.py
        follow.py
        pcost.py
        portfolio.py
        report.py
        stock.py
        tableformat.py
        ticker.py
        typedproperty.py
```
