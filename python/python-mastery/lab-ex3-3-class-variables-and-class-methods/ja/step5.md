# 汎用化

クラスメソッドの便利な機能の 1 つは、幅広いクラスに対して非常に一貫したインスタンス作成インターフェイスを提供し、それを使用する汎用のユーティリティ関数を書くことができるということです。

以前、CSV データを読み取るいくつかの関数がある`reader.py`ファイルを作成しました。次の`read_csv_as_instances()`関数をファイルに追加します。この関数はクラスを入力として受け取り、クラスの`from_row()`メソッドを使用してインスタンスのリストを作成します。

```python
# reader.py
...

def read_csv_as_instances(filename, cls):
    '''
    CSV ファイルをインスタンスのリストに読み込む
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records
```

`read_portfolio()`関数を削除します。もはや必要ありません。`Stock`オブジェクトのリストを読み取りたい場合は、次のようにします。

```python
>>> # Read a portfolio of Stock instances
>>> from reader import read_csv_as_instances
>>> from stock import Stock
>>> portfolio = read_csv_as_instances('portfolio.csv', Stock)
>>> portfolio
[<__main__.Stock object at 0x100674748>,
<__main__.Stock object at 0x1006746d8>,
<__main__.Stock object at 0x1006747b8>,
<__main__.Stock object at 0x100674828>,
<__main__.Stock object at 0x100674898>,
<__main__.Stock object at 0x100674908>,
<__main__.Stock object at 0x100674978>]
>>>
```

`read_csv_as_instances()`をまったく異なるクラスで使用する方法の別の例を次に示します。

```python
>>> class Row:
         def __init__(self, route, date, daytype, numrides):
             self.route = route
             self.date = date
             self.daytype = daytype
             self.numrides = numrides
         @classmethod
         def from_row(cls, row):
             return cls(row[0], row[1], row[2], int(row[3]))

>>> rides = read_csv_as_instances('ctabus.csv', Row)
>>> len(rides)
577563
>>>
```

**考察**

この実験は、クラス変数とクラスメソッドの最も一般的な 2 つの使い方を示しています。クラス変数は、すべてのインスタンスで共有されるグローバルパラメータ（たとえば、設定セッティング）を保持するためによく使用されます。時々、サブクラスは基底クラスから継承し、設定をオーバーライドして動作を変更します。

クラスメソッドは、示したように代替コンストラクタを実装するために最も一般的に使用されます。このようなクラスメソッドを見つける一般的な方法は、名前の中に「from」という単語があるかどうかを見ることです。たとえば、次は組み込み辞書の例です。

```python
>>> d = dict.fromkeys(['a','b','c'], 0)     # class method
>>> d
{'a': 0, 'c': 0, 'b': 0}
>>>
```
