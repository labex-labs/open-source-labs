# Exercise 6.11: Filtering data

Write a function that filters data. For example:

```python
# ticker.py
...

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row
```

Use this to filter stocks to just those in your portfolio:

```python
import report
portfolio = report.read_portfolio('portfolio.csv')
rows = parse_stock_data(follow('stocklog.csv'))
rows = filter_symbols(rows, portfolio)
for row in rows:
    print(row)
```
