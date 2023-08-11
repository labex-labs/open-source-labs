# Exercise 4.9: Better output for printing objects

Modify the `Stock` object that you defined in `stock.py` so that the `__repr__()` method produces more useful output. For example:

```python
>>> goog = Stock('GOOG', 100, 490.1)
>>> goog
Stock('GOOG', 100, 490.1)
>>>
```

See what happens when you read a portfolio of stocks and view the resulting list after you have made these changes. For example:

```python
>>> import report
>>> portfolio = report.read_portfolio('portfolio.csv')
>>> portfolio
... see what the output is ...
>>>
```
