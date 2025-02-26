# 準備

始める前に、もう少し単純なデータセット（保有株式のポートフォリオ）を使って基本を復習しましょう。`readport.py` というファイルを作成し、このコードを入れます。

```python
# readport.py

import csv

# ファイルを辞書のリストに読み込む関数
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {
                'name' : row[0],
               'shares' : int(row[1]),
                'price' : float(row[2])
            }
            portfolio.append(record)
    return portfolio
```

このファイルは `portfolio.csv` というファイルにある単純な株価データを読み込みます。この関数を使ってファイルを読み込み、結果を見てみましょう。

Pythonシェルを開き、次のことを試してみます。

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> from pprint import pprint
>>> pprint(portfolio)
[{'name': 'AA', 'price': 32.2,'shares': 100},
 {'name': 'IBM', 'price': 91.1,'shares': 50},
 {'name': 'CAT', 'price': 83.44,'shares': 150},
 {'name': 'MSFT', 'price': 51.23,'shares': 200},
 {'name': 'GE', 'price': 40.37,'shares': 95},
 {'name': 'MSFT', 'price': 65.1,'shares': 50},
 {'name': 'IBM', 'price': 70.44,'shares': 100}]
>>>
```

このデータでは、各行は株式名、保有株数、購入価格で構成されています。MSFTやIBMなどの特定の株式名には複数のエントリがあります。
