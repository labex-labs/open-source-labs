# Exercise 3.2: Creating a top-level function for program execution

Take the last part of your program and package it into a single function `portfolio_report(portfolio_filename, prices_filename)`. Have the function work so that the following function call creates the report as before:

```python
portfolio_report('/home/labex/project/portfolio.csv', '/home/labex/project/prices.csv')
```

In this final version, your program will be nothing more than a series of function definitions followed by a single function call to `portfolio_report()` at the very end (which executes all of the steps involved in the program).

By turning your program into a single function, it becomes easy to run it on different inputs. For example, try these statements interactively after running your program:

```python
>>> portfolio_report('/home/labex/project/portfolio2.csv', '/home/labex/project/prices.csv')
... look at the output ...
>>> files = ['/home/labex/project/portfolio.csv', '/home/labex/project/portfolio2.csv']
>>> for name in files:
        print(f'{name:-^43s}')
        portfolio_report(name, '/home/labex/project/prices.csv')
        print()

... look at the output ...
>>>
```
