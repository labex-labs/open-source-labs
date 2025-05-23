# 演習 2.6：辞書をコンテナとして使用する

辞書は、整数以外のインデックスを使って項目を検索したい場合に便利な方法です。Python シェルで辞書を試してみましょう：

```python
>>> prices = { }
>>> prices['IBM'] = 92.45
>>> prices['MSFT'] = 45.12
>>> prices
... 結果を見る...
>>> prices['IBM']
92.45
>>> prices['AAPL']
... 結果を見る...
>>> 'AAPL' in prices
False
>>>
```

`prices.csv` ファイルには、株価の一連の行が含まれています。このファイルはこのようになっています：

```csv
"AA",9.22
"AXP",24.85
"BA",44.85
"BAC",11.27
"C",3.72
...
```

辞書のキーが株式名で、辞書の値が株価であるように、このような価格のセットを読み取る関数 `read_prices(filename)` を書きましょう。

これを行うには、空の辞書から始めて、上記と同じように値を挿入し始めます。ただし、今回はファイルから値を読み取っています。

このデータ構造を使って、与えられた株式名の価格を迅速に検索します。

この部分で必要になるいくつかの小さなヒントがあります。まず、前と同じように `csv` モジュールを使うことを確認してください。ここでは再発明する必要はありません。

```python
>>> import csv
>>> f = open('/home/labex/project/prices.csv', 'r')
>>> rows = csv.reader(f)
>>> for row in rows:
        print(row)


['AA', '9.22']
['AXP', '24.85']
...
[]
>>>
```

もう 1 つの小さな問題は、`prices.csv` ファイルに空行が含まれている可能性があることです。上記のデータの最後の行が空のリストであることに注意してください。これは、その行にデータが存在しなかったことを意味します。

これがプログラムを例外で終了させる原因になる可能性があります。`try` と `except` 文を使って、適切にこれをキャッチしましょう。考えてみましょう：`if` 文を使って不適切なデータを防ぐ方が良いでしょうか？

`read_prices()` 関数を書いたら、対話的にテストして、機能することを確認しましょう：

```python
>>> prices = read_prices('/home/labex/project/prices.csv')
>>> prices['IBM']
106.28
>>> prices['MSFT']
20.89
>>>
```
