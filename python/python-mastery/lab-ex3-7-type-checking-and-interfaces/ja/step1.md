# インターフェイスと型チェッキング

`print_table()` 関数を変更して、提供されたフォーマッターインスタンスが `TableFormatter` から継承しているかどうかをチェックします。継承していない場合は、`TypeError` を発生させます。

新しいコードはこのような状況をキャッチする必要があります。

```python
>>> import stock, reader, tableformat
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> class MyFormatter:
        def headings(self,headers): pass
        def row(self,rowdata): pass

>>> tableformat.print_table(portfolio, ['name','shares','price'], MyFormatter())
Traceback (most recent call last):
...
TypeError: Expected a TableFormatter
>>>
```

このようなチェックを追加することで、プログラムにある程度の安全性が追加されます。ただし、Pythonでは型チェッキングが比較的弱いことに注意する必要があります。適切な基底クラスから継承している場合でも、フォーマッターとして渡されるオブジェクトが正しく機能することは保証されません。次の部分では、その問題に対処します。
