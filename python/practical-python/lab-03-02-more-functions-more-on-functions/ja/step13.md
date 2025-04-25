# 演習 3.3: CSV ファイルの読み取り

まずは、CSV ファイルを辞書のリストに読み込む問題に焦点を当てましょう。`fileparse_3.3.py` ファイルに、次のような関数を定義します。

```python
# fileparse_3.3.py
import csv

def parse_csv(filename):
    '''
    CSV ファイルをレコードのリストに解析する
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # ファイルのヘッダーを読む
        headers = next(rows)
        records = []
        for row in rows:
            if not row:    # データのない行をスキップ
                continue
            record = dict(zip(headers, row))
            records.append(record)

    return records
```

この関数は、ファイルを開く詳細、`csv` モジュールでラップすること、空行を無視することなどの詳細を隠しながら、CSV ファイルを辞書のリストに読み込みます。

試してみましょう。

ヒント：`python3 -i fileparse_3.3.py`。

```python
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv')
>>> portfolio
[{'name': 'AA','shares': '100', 'price': '32.20'}, {'name': 'IBM','shares': '50', 'price': '91.10'}, {'name': 'CAT','shares': '150', 'price': '83.44'}, {'name': 'MSFT','shares': '200', 'price': '51.23'}, {'name': 'GE','shares': '95', 'price': '40.37'}, {'name': 'MSFT','shares': '50', 'price': '65.10'}, {'name': 'IBM','shares': '100', 'price': '70.44'}]
>>>
```

これは良いですが、すべてが文字列として表されているため、データを使って何か有益な計算を行うことはできません。これをすぐに修正しますが、それに引き続き作り上げていきましょう。
