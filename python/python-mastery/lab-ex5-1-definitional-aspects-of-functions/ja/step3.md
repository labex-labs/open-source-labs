# 柔軟性について考える

今のところ、`reader.py`内の2つの関数は、直接`open()`に渡されるファイル名で動作するようにハードコードされています。コードをリファクタリングして、行を生成する任意の反復可能オブジェクトで動作するようにしましょう。これを行うには、行の任意の反復可能なシーケンスを変換する2つの新しい関数`csv_as_dicts(lines, types)`と`csv_as_instances(lines, cls)`を作成します。たとえば：

```python
>>> file = open('portfolio.csv')
>>> port = reader.csv_as_dicts(file, [str, int, float])
>>> port
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1},
 {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'MSFT','shares': 200, 'price': 51.23},
 {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1},
 {'name': 'IBM','shares': 100, 'price': 70.44}]
>>>
```

これを行う主な目的は、さまざまな種類の入力ソースで動作できるようにすることです。たとえば：

```python
>>> import gzip
>>> import stock
>>> file = gzip.open('portfolio.csv.gz')
>>> port = reader.csv_as_instances(file, stock.Stock)
>>> port
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44),
 Stock('MSFT', 200, 51.23), Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.1),
 Stock('IBM', 100, 70.44)]
>>>
```

古いコードとの互換性を維持するために、以前と同じようにファイル名を受け取る関数`read_csv_as_dicts()`と`read_csv_as_instances()`を書きます。これらの関数は、提供されたファイル名で`open()`を呼び出し、結果のファイルで新しい`csv_as_dicts()`または`csv_as_instances()`関数を使用する必要があります。
