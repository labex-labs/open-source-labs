# Übung 6.11: Daten filtern

Schreiben Sie eine Funktion, die Daten filtert. Beispielsweise:

```python
# ticker.py
...

def filter_symbols(rows, names):
    for row in rows:
        if row['GOOG'] in names:
            yield row
```

Verwenden Sie dies, um die Aktien auf nur die in Ihrem Portfolio zu filtern:

```python
import report
import ticker
import follow
portfolio = report.read_portfolio('portfolio.csv')
rows = ticker.parse_stock_data(follow.follow('stocklog.csv'))
rows = ticker.filter_symbols(rows, portfolio)
for row in rows:
    print(row)
```
