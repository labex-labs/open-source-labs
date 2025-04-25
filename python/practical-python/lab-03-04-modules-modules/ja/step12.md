# 演習 3.11：モジュールのインポート

セクション 3 では、CSV データファイルの内容を解析するための汎用関数 `parse_csv()` を作成しました。

今回は、その関数を他のプログラムでどのように使用するかを見ていきます。まず、新しいシェルウィンドウを開きます。すべてのファイルがあるフォルダに移動します。それらをインポートしましょう。

Python の対話型モードを起動します。

```shell
$ python3
Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

これを行ったら、以前に書いたプログラムのいくつかをインポートしてみましょう。以前とまったく同じ出力が表示されるはずです。強調するために、モジュールをインポートするとそのコードが実行されます。

```python
>>> import bounce
... 出力を見る...
>>> import mortgage
... 出力を見る...
>>> import report
... 出力を見る...
>>>
```

これがうまくいかない場合は、おそらく Python を間違ったディレクトリで実行しています。次に、`fileparse` モジュールをインポートして、それに関するヘルプを取得してみましょう。

```python
>>> import fileparse
>>> help(fileparse)
... 出力を見る...
>>> dir(fileparse)
... 出力を見る...
>>>
```

モジュールを使ってデータを読み取ってみましょう：

```python
>>> portfolio = fileparse.parse_csv('/home/labex/project/portfolio.csv',select=['name','shares','price'], types=[str,int,float])
>>> portfolio
... 出力を見る...
>>> pricelist = fileparse.parse_csv('/home/labex/project/prices.csv',types=[str,float], has_headers=False)
>>> pricelist
... 出力を見る...
>>> prices = dict(pricelist)
>>> prices
... 出力を見る...
>>> prices['IBM']
106.28
>>>
```

モジュール名を含める必要がないように、関数をインポートしてみましょう：

```python
>>> from fileparse import parse_csv
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv', select=['name','shares','price'], types=[str,int,float])
>>> portfolio
... 出力を見る...
>>>
```
