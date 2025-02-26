# テーブル出力

演習3.1では、整った形式のテーブルを作成する関数 `print_portfolio()` を書きました。その関数は `Stock` オブジェクトのリストに対してカスタマイズされていました。しかし、(b)の技術を使って、任意のオブジェクトのリストで動作するように完全に汎用化することができます。

`tableformat.py` という新しいモジュールを作成します。そのプログラムでは、オブジェクトのシーケンス（リスト）、属性名のリストを受け取り、整った形式のテーブルを出力する関数 `print_table()` を書きます。たとえば：

```python
>>> import stock
>>> import tableformat
>>> portfolio = stock.read_portfolio('portfolio.csv')
>>> tableformat.print_table(portfolio, ['name','shares','price'])
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44

>>> tableformat.print_table(portfolio,['shares','name'])
    shares       name
---------- ----------
       100         AA
        50        IBM
       150        CAT
       200       MSFT
        95         GE
        50       MSFT
       100        IBM
>>>
```

簡単のために、`print_table()` 関数は各フィールドを10文字幅の列で出力するだけにします。
