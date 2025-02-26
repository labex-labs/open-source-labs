# 解析ユーティリティ関数の作成

新しいファイル `reader.py` を作成します。そのファイルに、CSVデータのファイルを各列の型変換をユーザーが指定した辞書のリストに読み込むユーティリティ関数 `read_csv_as_dicts()` を定義します。

動作方法は以下の通りです。

```python
>>> import reader
>>> portfolio = reader.read_csv_as_dicts('portfolio.csv', [str,int,float])
>>> for s in portfolio:
         print(s)

{'name': 'AA','shares': 100, 'price': 32.2}
{'name': 'IBM','shares': 50, 'price': 91.1}
{'name': 'CAT','shares': 150, 'price': 83.44}
{'name': 'MSFT','shares': 200, 'price': 51.23}
{'name': 'GE','shares': 95, 'price': 40.37}
{'name': 'MSFT','shares': 50, 'price': 65.1}
{'name': 'IBM','shares': 100, 'price': 70.44}
>>>
```

または、CTAデータを読み取りたい場合：

```python
>>> rows = reader.read_csv_as_dicts('ctabus.csv', [str,str,str,int])
>>> len(rows)
577563
>>> rows[0]
{'daytype': 'U', 'route': '3', 'rides': 7354, 'date': '01/01/2001'}
>>>
```
