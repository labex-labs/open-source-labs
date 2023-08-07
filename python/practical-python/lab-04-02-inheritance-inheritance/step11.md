# Multiple Inheritance

You can inherit from multiple classes by specifying them in the definition of the class.

```python
class Mother:
    ...

class Father:
    ...

class Child(Mother, Father):
    ...
```

The class `Child` inherits features from both parents. There are some rather tricky details. Don't do it unless you know what you are doing. Some further information will be given in the next section, but we're not going to utilize multiple inheritance further in this course.

A major use of inheritance is in writing code that's meant to be extended or customized in various ways--especially in libraries or frameworks. To illustrate, consider the `print_report()` function in your `report.py` program. It should look something like this:

```python
def print_report(reportdata):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''
    headers = ('Name','Shares','Price','Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ')*len(headers))
    for row in reportdata:
        print('%10s %10d %10.2f %10.2f' % row)
```

When you run your report program, you should be getting output like this:

```python
>>> import report
>>> report.portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
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
