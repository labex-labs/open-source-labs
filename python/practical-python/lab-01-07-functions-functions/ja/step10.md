# 演習 1.33：コマンドラインからの読み取り

`pcost.py` プログラムでは、入力ファイルの名前がコードに直接埋め込まれています：

```python
# pcost.py

def portfolio_cost(filename):
 ...
    # ここにコードを記述
 ...

cost = portfolio_cost('portfolio.csv')
print('Total cost:', cost)
```

学習やテストには問題ありませんが、本番のプログラムではおそらくそうはしません。

代わりに、ファイル名を引数としてスクリプトに渡すことができます。プログラムの下部を次のように変更してみてください：

```python
# pcost_1.33.py

import csv


def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)  # ヘッダー行をスキップ
        for row in rows:
            if len(row) < 3:
                print("Skipping invalid row:", row)
                continue
            try:
                nshares = int(row[1])
                price = float(row[2])
                total_cost += nshares * price
            except (IndexError, ValueError):
                print("Skipping invalid row:", row)

    return total_cost

import sys


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)
```

`sys.argv` は、コマンドライン上で渡された引数（あれば）を含むリストです。

プログラムを実行するには、ターミナルから Python を実行する必要があります。

たとえば、Unix の bash から：

```bash
$ python3 pcost.py portfolio.csv
Total cost: 44671.15
bash %
```
