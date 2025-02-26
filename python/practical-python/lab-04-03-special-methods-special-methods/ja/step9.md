# 演習 4.10：getattr() の使用例

`getattr()` は属性を読み取るための代替メカニズムです。非常に柔軟なコードを書くために使用できます。まずは、この例を試してみましょう：

```python
>>> import stock
>>> s = stock.Stock('GOOG', 100, 490.1)
>>> columns = ['name','shares']
>>> for colname in columns:
        print(colname, '=', getattr(s, colname))

name = GOOG
shares = 100
>>>
```

出力データが、`columns` 変数にリストされた属性名に完全によって決まることに注意深く観察してください。

`tableformat.py` ファイルで、この考えを取り上げて、任意のオブジェクトのリストのユーザ指定属性を表示するテーブルを印刷する汎用関数 `print_table()` に拡張します。以前の `print_report()` 関数と同様に、`print_table()` も出力形式を制御するために `TableFormatter` インスタンスを受け取る必要があります。以下がその動作方法です：

```python
>>> import report
>>> portfolio = report.read_portfolio('portfolio.csv')
>>> from tableformat import create_formatter, print_table
>>> formatter = create_formatter('txt')
>>> print_table(portfolio, ['name','shares'], formatter)
      name     shares
---------- ----------
        AA        100
       IBM         50
       CAT        150
      MSFT        200
        GE         95
      MSFT         50
       IBM        100

>>> print_table(portfolio, ['name','shares', 'price'], formatter)
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
>>>
```
