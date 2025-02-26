# 演習6.11: データのフィルタリング

データをフィルタリングする関数を書きます。たとえば：

```python
# ticker.py
...

def filter_symbols(rows, names):
    for row in rows:
        if row['GOOG'] in names:
            yield row
```

これを使って、ポートフォリオに含まれる銘柄のみにデータをフィルタリングします。

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
