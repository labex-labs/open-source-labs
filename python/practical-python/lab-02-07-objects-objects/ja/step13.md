# 演習 2.26: 全体像

この演習で学んだ手法を使えば、ほとんどの列指向データファイルのフィールドを簡単に Python の辞書に変換する文を書けます。

例を挙げるために、別のデータファイルからデータを読み取るとしましょう。

```python
>>> f = open('dowstocks.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> row = next(rows)
>>> headers
['name', 'price', 'date', 'time', 'change', 'open', 'high', 'low', 'volume']
>>> row
['AA', '39.48', '6/11/2007', '9:36am', '-0.18', '39.67', '39.69', '39.45', '181800']
>>>
```

同じようなトリックを使ってフィールドを変換してみましょう。

```python
>>> types = [str, float, str, str, float, float, float, float, int]
>>> converted = [func(val) for func, val in zip(types, row)]
>>> record = dict(zip(headers, converted))
>>> record
{'volume': 181800, 'name': 'AA', 'price': 39.48, 'high': 39.69,
'low': 39.45, 'time': '9:36am', 'date': '6/11/2007', 'open': 39.67,
'change': -0.18}
>>> record['name']
'AA'
>>> record['price']
39.48
>>>
```

ボーナス：この例をどのように変更すれば、`date` エントリを `(6, 11, 2007)` のようなタプルに追加でパースできるようになりますか？

この演習で行ったことを少し考えてみましょう。後ほどこれらのアイデアに戻ります。
