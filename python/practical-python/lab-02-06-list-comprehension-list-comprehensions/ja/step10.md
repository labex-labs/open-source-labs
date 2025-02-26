# 演習2.23: CSVファイルからのデータ抽出

リスト、セット、辞書内包表記のさまざまな組み合わせをどのように使うかを知ることは、さまざまな形式のデータ処理に役立ちます。ここでは、CSVファイルから選択された列を抽出する方法を示す例を紹介します。

まず、CSVファイルからヘッダー情報の1行を読み取ります。

```python
>>> import csv
>>> f = open('portfoliodate.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> headers
['name', 'date', 'time','shares', 'price']
>>>
```

次に、実際に関心のある列をリストに格納する変数を定義します。

```python
>>> select = ['name','shares', 'price']
>>>
```

次に、上記の列がソースCSVファイルのどのインデックスにあるかを特定します。

```python
>>> indices = [ headers.index(colname) for colname in select ]
>>> indices
[0, 3, 4]
>>>
```

最後に、1行のデータを読み取り、辞書内包表記を使って辞書に変換します。

```python
>>> row = next(rows)
>>> record = { colname: row[index] for colname, index in zip(select, indices) }   # dict-comprehension
>>> record
{'price': '32.20', 'name': 'AA','shares': '100'}
>>>
```

これまでのことが分かりやすければ、ファイルの残りを読み取りましょう。

```python
>>> portfolio = [ { colname: row[index] for colname, index in zip(select, indices) } for row in rows ]
>>> portfolio
[{'price': '91.10', 'name': 'IBM','shares': '50'}, {'price': '83.44', 'name': 'CAT','shares': '150'},
  {'price': '51.23', 'name': 'MSFT','shares': '200'}, {'price': '40.37', 'name': 'GE','shares': '95'},
  {'price': '65.10', 'name': 'MSFT','shares': '50'}, {'price': '70.44', 'name': 'IBM','shares': '100'}]
>>>
```

まあ、あなたはちょうど`read_portfolio()`関数の多くを1つの文にまとめました。
