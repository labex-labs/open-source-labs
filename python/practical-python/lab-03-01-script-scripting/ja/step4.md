# 関数の定義

単一の「タスク」に関連するコードをすべて一箇所にまとめるのは良い考えです。関数を使いましょう。

```python
def read_prices(filename):
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices
```

関数はまた、繰り返しの操作を簡略化します。

```python
oldprices = read_prices('oldprices.csv')
newprices = read_prices('newprices.csv')
```
