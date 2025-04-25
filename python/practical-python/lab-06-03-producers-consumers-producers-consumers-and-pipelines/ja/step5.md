# 演習 6.10: さらに多くのパイプラインコンポーネントを作成する

全体的な考え方をさらに大きなパイプラインに拡張しましょう。別のファイル `ticker.py` で、上で行ったように CSV ファイルを読み取る関数を作成します。

```python
# ticker.py

from follow import follow
import csv

def parse_stock_data(lines):
    rows = csv.reader(lines)
    return rows

if __name__ == '__main__':
    lines = follow('stocklog.csv')
    rows = parse_stock_data(lines)
    for row in rows:
        print(row)
```

特定の列を選択する新しい関数を書きます。

    # ticker.py

...
def select_columns(rows, indices):
for row in rows:
yield [row[index] for index in indices]
...
def parse_stock_data(lines):
rows = csv.reader(lines)
rows = select_columns(rows, [0, 1, 4])
return rows

再度プログラムを実行します。このように出力が絞られたものが表示されるはずです。

    ['GOOG', '1503.06', '2.81']
    ['AAPL', '253.31', '2.81']
    ['GOOG', '1503.07', '2.82']
    ['AAPL', '253.32', '2.82']
    ['GOOG', '1503.08', '2.83']

...

データ型を変換し、辞書を作成するジェネレータ関数を書きます。たとえば：

```python
# ticker.py
...

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))
...
def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows
...
```

再度プログラムを実行します。このような辞書のストリームが表示されるはずです。

    {'name': 'GOOG', 'price': 1503.4, 'change': 3.15}
    {'name': 'AAPL', 'price': 253.65, 'change': 3.15}
    {'name': 'GOOG', 'price': 1503.41, 'change': 3.16}
    {'name': 'AAPL', 'price': 253.66, 'change': 3.16}
    {'name': 'GOOG', 'price': 1503.42, 'change': 3.17}
    {'name': 'AAPL', 'price': 253.67, 'change': 3.17}

...
