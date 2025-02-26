# Ejercicio 6.11: Filtrando datos

Escribe una función que filtre datos. Por ejemplo:

```python
# ticker.py
...

def filter_symbols(rows, names):
    for row in rows:
        if row['GOOG'] in names:
            yield row
```

Utiliza esto para filtrar las acciones solo a aquellas en tu cartera:

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
