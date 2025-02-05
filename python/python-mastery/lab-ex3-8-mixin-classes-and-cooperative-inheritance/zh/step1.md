# 列格式化的问题

如果你回溯到练习3.1，你编写了一个函数`print_portfolio()`，它生成了如下这样的表格：

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

在过去几个练习中开发的`print_table()`函数几乎取代了这个功能 —— 几乎。它存在的一个问题是，它无法精确格式化每列的内容。例如，注意`price`列中的值是如何精确格式化为保留两位小数的。`TableFormatter`类及相关子类做不到这一点。

一种解决方法是修改`print_table()`函数，使其接受一个额外的`formats`参数。例如，可能像这样：

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

是的，你可以像这样修改`print_table()`，但这是正确的做法吗？所有`TableFormatter`类的整个理念是它们可以在不同类型的应用中使用。列格式化在其他地方可能也有用，而不仅仅在`print_table()`函数中。

另一种可能的方法是某种程度上改变`TableFormatter`类的接口。例如，也许添加第三个方法来应用格式化。

```python
class TableFormatter:
    def headings(self, headers):
     ...
    def format(self, rowdata):
     ...
    def row(self, rowdata):
     ...
```

这里的问题是，每当你改变一个类的接口时，你都必须重构所有现有的代码以使其与之配合。具体来说，你必须修改所有已经编写的`TableFormatter`子类以及所有为使用它们而编写的代码。我们不要这样做。

作为替代方案，用户可以使用继承来定制特定的格式化器，以便将一些格式化注入其中。例如，试试这个实验：

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

是的，这可行，但也有点笨拙和奇怪。用户必须选择一个特定的格式化器来定制。除此之外，他们还必须自己实现实际的列格式化代码。肯定有其他不同的方法来做到这一点。
