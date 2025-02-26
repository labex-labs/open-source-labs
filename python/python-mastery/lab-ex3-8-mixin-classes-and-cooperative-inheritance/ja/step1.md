# 列のフォーマットに関する問題

演習3.1に戻ると、次のような表を生成する関数`print_portfolio()`を書きました。

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> print_portfolio(portfolio)
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
>>>
```

過去数回の演習で開発された`print_table()`関数は、この機能をほぼ置き換えますが、ほぼです。その1つの問題は、各列の内容を正確にフォーマットできないことです。たとえば、`price`列の値が2桁の小数で正確にフォーマットされていることに注目してください。`TableFormatter`クラスと関連するサブクラスはそれができません。

これを修正する1つの方法は、`print_table()`関数を修正して、追加の`formats`引数を受け取るようにすることです。たとえば、次のようなものかもしれません。

```python
>>> def print_table(records, fields, formats, formatter):
        formatter.headings(fields)
        for r in records:
            rowdata = [(fmt % getattr(r, fieldname))
                 for fieldname,fmt in zip(fields,formats)]
            formatter.row(rowdata)

>>> import stock, reader
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> from tableformat import TextTableFormatter
>>> formatter = TextTableFormatter()
>>> print_table(portfolio,
                ['name','shares','price'],
                ['%s','%d','%0.2f'],
                formatter)

      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
>>>
```

はい、`print_table()`をこのように修正できますが、それが適切な場所でしょうか？すべての`TableFormatter`クラスの全体的な考え方は、さまざまな種類のアプリケーションで使用できるということです。列のフォーマットは、`print_table()`関数だけでなく、他の場所でも役立つ可能性があります。

別の考えられるアプローチは、`TableFormatter`クラスのインターフェイスを何らかの方法で変更することかもしれません。たとえば、フォーマットを適用するための3番目のメソッドを追加するかもしれません。

```python
class TableFormatter:
    def headings(self, headers):
     ...
    def format(self, rowdata):
     ...
    def row(self, rowdata):
     ...
```

ここでの問題は、クラスのインターフェイスを変更するたびに、既存のコード全体をそれに対応するように再構築しなければならないということです。具体的には、既に書かれたすべての`TableFormatter`サブクラスと、それらを使用するために書かれたすべてのコードを修正しなければなりません。それはしません。

代替策として、ユーザーは継承を使用して特定のフォーマッタをカスタマイズして、そこにいくつかのフォーマットを注入することができます。たとえば、この実験を試してみてください。

```python
>>> from tableformat import TextTableFormatter, print_table
>>> class PortfolioFormatter(TextTableFormatter):
        def row(self, rowdata):
            formats = ['%s','%d','%0.2f']
            rowdata = [(fmt % d) for fmt, d in zip(formats, rowdata)]
            super().row(rowdata)

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
>>>
```

はい、それは機能しますが、少し不器用で奇妙です。ユーザーはカスタマイズするために特定のフォーマッタを選ばなければなりません。その上、彼らは実際の列のフォーマットコードを自分たちで実装しなければなりません。確かに、これを行う別の方法があります。
