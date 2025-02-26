# 前回の実験

前回の実験で定義された`Stock`クラスのインスタンスは通常、次のように作成されます。

```python
>>> s = Stock('GOOG', 100, 490.1)
>>>
```

ただし、`read_portfolio()`関数はまた、ファイルから読み取ったデータの行からインスタンスを作成します。たとえば、次のようなコードが使用されます。

```python
>>> import csv
>>> f = open('portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>> s = Stock(row[0], int(row[1]), float(row[2]))
>>>
```
