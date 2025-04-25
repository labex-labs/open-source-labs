# 演習 3.4: 列選択機能の作成

多くの場合、CSV ファイルから選択された特定の列のみに興味があり、すべてのデータには興味がありません。`parse_csv()` 関数を次のように修正して、ユーザーが指定できる列を選択できるようにしましょう。

```python
>>> # すべてのデータを読む
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv')
>>> portfolio
[{'name': 'AA','shares': '100', 'price': '32.20'}, {'name': 'IBM','shares': '50', 'price': '91.10'}, {'name': 'CAT','shares': '150', 'price': '83.44'}, {'name': 'MSFT','shares': '200', 'price': '51.23'}, {'name': 'GE','shares': '95', 'price': '40.37'}, {'name': 'MSFT','shares': '50', 'price': '65.10'}, {'name': 'IBM','shares': '100', 'price': '70.44'}]

>>> # 一部のデータのみを読む
>>> shares_held = parse_csv('/home/labex/project/portfolio.csv', select=['name','shares'])
>>> shares_held
[{'name': 'AA','shares': '100'}, {'name': 'IBM','shares': '50'}, {'name': 'CAT','shares': '150'}, {'name': 'MSFT','shares': '200'}, {'name': 'GE','shares': '95'}, {'name': 'MSFT','shares': '50'}, {'name': 'IBM','shares': '100'}]
>>>
```

演習 2.23 で列選択機能の例が示されています。ただし、実装方法の 1 つは次の通りです。

```python
# fileparse_3.4.py
import csv

def parse_csv(filename, select=None):
    '''
    CSV ファイルをレコードのリストに解析する
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # ファイルのヘッダーを読む
        headers = next(rows)

        # 列選択機能が指定されている場合、指定された列のインデックスを見つけます。
        # 結果の辞書に使用するヘッダーのセットも絞り込みます。
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:    # データのない行をスキップ
                continue
            # 特定の列が選択されている場合、行をフィルタリングします
            if indices:
                row = [ row[index] for index in indices ]

            # 辞書を作成
            record = dict(zip(headers, row))
            records.append(record)

    return records
```

この部分にはいくつかのポイントがあります。おそらく最も重要なのは、列選択を行インデックスにマッピングすることです。たとえば、入力ファイルに次のようなヘッダーがあったとしましょう。

```python
>>> headers = ['name', 'date', 'time','shares', 'price']
>>>
```

次に、選択された列が次のようであったとします。

```python
>>> select = ['name','shares']
>>>
```

適切な選択を行うには、選択された列名をファイル内の列インデックスにマッピングする必要があります。このステップが行っているのがこれです。

```python
>>> indices = [headers.index(colname) for colname in select ]
>>> indices
[0, 3]
>>>
```

言い換えると、"name" は列 0 で、"shares" は列 3 です。ファイルからデータの行を読むとき、インデックスを使ってそれをフィルタリングします。

```python
>>> row = ['AA', '6/11/2007', '9:50am', '100', '32.20' ]
>>> row = [ row[index] for index in indices ]
>>> row
['AA', '100']
>>>
```
