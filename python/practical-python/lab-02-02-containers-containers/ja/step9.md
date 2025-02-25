# 演習2.4：タプルのリスト

`portfolio.csv` ファイルには、ポートフォリオ内の株式のリストが含まれています。演習1.30では、このファイルを読み取り、単純な計算を行う関数 `portfolio_cost(filename)` を書きました。

あなたのコードはおそらくこのようになっているはずです。

```python
# pcost.py

import csv

def portfolio_cost(filename):
    '''ポートフォリオファイルの総コスト（株数 * 価格）を計算する'''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost
```

このコードを大まかなガイドとして、新しいファイル `report.py` を作成します。そのファイルに、与えられたポートフォリオファイルを開き、タプルのリストに読み込む関数 `read_portfolio(filename)` を定義します。これを行うには、上記のコードにいくつかの小さな修正を加えます。

まず、`total_cost = 0` を定義する代わりに、最初に空のリストに設定される変数を作成します。たとえば：

```python
portfolio = []
```

次に、コストを合算する代わりに、各行を前の演習とまったく同じようにタプルに変換し、このリストに追加します。たとえば：

```python
for row in rows:
    holding = (row[0], int(row[1]), float(row[2]))
    portfolio.append(holding)
```

最後に、結果の `portfolio` リストを返します。

対話的に関数を試してみましょう（これを行うには、まずインタプリタで `report.py` プログラムを実行する必要があることに注意してください）：

_ヒント：端末でファイルを実行する際に `-i` を使用します_

```python
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> portfolio
[('AA', 100, 32.2), ('IBM', 50, 91.1), ('CAT', 150, 83.44), ('MSFT', 200, 51.23),
    ('GE', 95, 40.37), ('MSFT', 50, 65.1), ('IBM', 100, 70.44)]
>>>
>>> portfolio[0]
('AA', 100, 32.2)
>>> portfolio[1]
('IBM', 50, 91.1)
>>> portfolio[1][1]
50
>>> total = 0.0
>>> for s in portfolio:
        total += s[1] * s[2]

>>> print(total)
44671.15
>>>
```

あなたが作成したこのタプルのリストは、2次元配列に非常に似ています。たとえば、`portfolio[row][column]` のような参照を使用して特定の列と行にアクセスできます。ここで `row` と `column` は整数です。

つまり、最後のforループをこのような文を使って書き直すこともできます：

```python
>>> total = 0.0
>>> for name, shares, price in portfolio:
            total += shares*price

>>> print(total)
44671.15
>>>
```
