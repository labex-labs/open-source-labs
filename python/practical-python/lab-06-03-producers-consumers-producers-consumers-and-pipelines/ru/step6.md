# Упражнение 6.11: Фильтрация данных

Напишите функцию, которая фильтрует данные. Например:

```python
# ticker.py
...

def filter_symbols(rows, names):
    for row in rows:
        if row['GOOG'] in names:
            yield row
```

Используйте это для фильтрации акций только тех, которые находятся в вашем портфеле:

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
