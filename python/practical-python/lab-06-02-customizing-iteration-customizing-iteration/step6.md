# Exercise 6.7: Watching your portfolio

Modify the `follow.py` program so that it watches the stream of stock data and prints a ticker showing information for only those stocks in a portfolio. For example:

```python
if __name__ == '__main__':
    import report

    portfolio = report.read_portfolio('portfolio.csv')

    for line in follow('stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```

Note: For this to work, your `Portfolio` class must support the `in` operator. See [Exercise 6.3](01_Iteration_protocol) and make sure you implement the `__contains__()` operator.
