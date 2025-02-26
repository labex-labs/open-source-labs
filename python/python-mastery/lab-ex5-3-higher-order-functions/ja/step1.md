# 高階関数の使用

現在、`reader.py` プログラムは2つのコア関数 `csv_as_dicts()` と `csv_as_instances()` で構成されています。これら2つの関数のコードはほぼ同じです。たとえば：

```python
def csv_as_dicts(lines, types, *, headers=None):
    '''
    CSV データの行を辞書のリストに変換する
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = { name: func(val)
                   for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines, cls, *, headers=None):
    '''
    CSV データの行をインスタンスのリストに変換する
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records
```

これらの関数のコア部分を、ユーザー定義の変換関数を引数として受け取る単一の関数 `convert_csv()` に統一します。たとえば：

```python
>>> def make_dict(headers, row):
        return dict(zip(headers, row))

>>> lines = open('portfolio.csv')
>>> convert_csv(lines, make_dict)
[{'name': 'AA','shares': '100', 'price': '32.20'}, {'name': 'IBM','shares': '50', 'price': '91.10'},
 {'name': 'CAT','shares': '150', 'price': '83.44'}, {'name': 'MSFT','shares': '200', 'price': '51.23'},
 {'name': 'GE','shares': '95', 'price': '40.37'}, {'name': 'MSFT','shares': '50', 'price': '65.10'},
 {'name': 'IBM','shares': '100', 'price': '70.44'}]
>>>
```

新しい `convert_csv()` 関数を使って、`csv_as_dicts()` と `csv_as_instances()` 関数を書き直します。
