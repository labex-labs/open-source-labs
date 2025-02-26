# 型アノテーション

関数定義にオプショナルな型ヒントを追加することもできます。

```python
def read_prices(filename: str) -> dict:
    '''
    Read prices from a CSV file of name,price data
    '''
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices
```

これらのヒントは実際の動作には何も影響しません。純粋に情報提供のみを目的としています。ただし、統合開発環境（IDE）、コードチェッカー、その他のツールでは、これらのヒントを利用してさらに多くのことを行うことができます。

第2節では、株式ポートフォリオのパフォーマンスを示すレポートを出力する `report.py` というプログラムを作成しました。このプログラムはいくつかの関数で構成されていました。たとえば：

```python
# report.py
import csv

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                'name' : record['name'],
               'shares' : int(record['shares']),
                'price' : float(record['price'])
            }
            portfolio.append(stock)
    return portfolio
...
```

ただし、プログラムには一連の手順通りの計算のみを行う部分もありました。このコードはプログラムの後半に現れました。たとえば：

```python
...

# Output the report

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s'  % headers)
print(('-' * 10 +'') * len(headers))
for row in report:
    print('%10s %10d %10.2f %10.2f' % row)
...
```

この演習では、このプログラムを取り上げて、関数の使用を中心にもう少し強力に整理します。
