# Using lambda

- lambda is highly restricted.
- Only a single expression is allowed.
- No statements like `if`, `while`, etc.
- Most common use is with functions like `sort()`.

Read some stock portfolio data and convert it into a list:

```python
>>> import report
>>> portfolio = list(report.read_portfolio('portfolio.csv'))
>>> for s in portfolio:
        print(s)

Stock('AA', 100, 32.2)
Stock('IBM', 50, 91.1)
Stock('CAT', 150, 83.44)
Stock('MSFT', 200, 51.23)
Stock('GE', 95, 40.37)
Stock('MSFT', 50, 65.1)
Stock('IBM', 100, 70.44)
>>>
```
