# 演習 2.5：辞書のリスト

演習 2.4 で書いた関数を取り、ポートフォリオ内の各株式をタプルではなく辞書で表すように修正します。この辞書では、入力ファイルの異なる列を表すために、「name」、「shares」、「price」のフィールド名を使用します。

演習 2.4 と同じ方法でこの新しい関数を試してみましょう。

```python
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> portfolio
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1},
    {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'MSFT','shares': 200, 'price': 51.23},
    {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1},
    {'name': 'IBM','shares': 100, 'price': 70.44}]
>>> portfolio[0]
{'name': 'AA','shares': 100, 'price': 32.2}
>>> portfolio[1]
{'name': 'IBM','shares': 50, 'price': 91.1}
>>> portfolio[1]['shares']
50
>>> total = 0.0
>>> for s in portfolio:
        total += s['shares']*s['price']

>>> print(total)
44671.15
>>>
```

ここでは、各エントリの異なるフィールドには、数値の列番号ではなくキー名を使ってアクセスすることがわかります。これは、結果のコードが後で読みやすくなるため、多くの場合好まれます。

大きな辞書やリストを表示すると混乱する場合があります。デバッグ用に出力を整理するには、`pprint` 関数を使用することを検討してください。

```python
>>> from pprint import pprint
>>> pprint(portfolio)
[{'name': 'AA', 'price': 32.2,'shares': 100},
    {'name': 'IBM', 'price': 91.1,'shares': 50},
    {'name': 'CAT', 'price': 83.44,'shares': 150},
    {'name': 'MSFT', 'price': 51.23,'shares': 200},
    {'name': 'GE', 'price': 40.37,'shares': 95},
    {'name': 'MSFT', 'price': 65.1,'shares': 50},
    {'name': 'IBM', 'price': 70.44,'shares': 100}]
>>>
```
