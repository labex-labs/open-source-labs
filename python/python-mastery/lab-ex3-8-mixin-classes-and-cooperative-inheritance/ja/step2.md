# 横方向への拡張

`tableformat.py`ファイルに、次のクラス定義を追加します。

```python
class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)
```

このクラスには、行の内容にフォーマットを適用する単一のメソッド`row()`が含まれています。クラス変数`formats`は、フォーマットコードを保持するために使用されます。このクラスは、多重継承を通じて使用されます。たとえば：

```python
>>> import stock, reader
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> from tableformat import TextTableFormatter, ColumnFormatMixin, print_table
>>> class PortfolioFormatter(ColumnFormatMixin, TextTableFormatter):
        formats = ['%s', '%d', '%0.2f']

>>> formatter = PortfolioFormatter()
>>> print_table(portfolio, ['name','shares','price'], formatter)
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

この全体的なアプローチが機能するのは、`ColumnFormatMixin`クラスが必要な`row()`メソッドを提供する別のクラスと一緒に混合されることを意図しているからです。

表のヘッダーを全て大文字で表示するフォーマッタを作成する別のクラスを作成します。

```python
class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])
```

これを試してみると、ヘッダーが現在大文字になっていることに気付きます。

```python
>>> from tableformat import TextTableFormatter, UpperHeadersMixin
>>> class PortfolioFormatter(UpperHeadersMixin, TextTableFormatter):
        pass

>>> formatter = PortfolioFormatter()
>>> print_table(portfolio, ['name','shares','price'], formatter)
      NAME     SHARES      PRICE
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

これが本当に「ミックスイン」の全体的な考え方です。ライブラリの作成者は、最初に`TextTableFormatter`、`CSVTableFormatter`などの基本的なクラスセットを提供することができます。その後、それらのクラスが異なる方法で動作するようにするための追加クラスのコレクションを提供することができます。
