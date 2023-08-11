# Exercise 9.2: Making an application directory

Putting all of your code into a "package" isn't often enough for an application. Sometimes there are supporting files, documentation, scripts, and other things. These files need to exist OUTSIDE of the `porty/` directory you made above.

Create a new directory called `porty-app`. Move the `porty` directory you created in Exercise 9.1 into that directory. Copy the `portfolio.csv` and `prices.csv` test files into this directory. Additionally create a `README.txt` file with some information about yourself. Your code should now be organized as follows:

    porty-app/
        portfolio.csv
        prices.csv
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

To run your code, you need to make sure you are working in the top-level `porty-app/` directory. For example, from the terminal:

```python
shell % cd porty-app
shell % python3
>>> import porty.report
>>>
```

Try running some of your prior scripts as a main program:

```python
shell % cd porty-app
shell % python3 -m porty.report portfolio.csv prices.csv txt
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
