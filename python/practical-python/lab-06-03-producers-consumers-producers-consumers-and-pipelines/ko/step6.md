# 연습 6.11: 데이터 필터링

데이터를 필터링하는 함수를 작성합니다. 예를 들어:

```python
# ticker.py
...

def filter_symbols(rows, names):
    for row in rows:
        if row['GOOG'] in names:
            yield row
```

이것을 사용하여 포트폴리오에 있는 주식만 필터링합니다.

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
