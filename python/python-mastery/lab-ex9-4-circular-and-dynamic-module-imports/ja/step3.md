# サブクラス登録

次の実験を行ってみて、観察してください。

```python
>>> from structly.tableformat.formats.text import TextTableFormatter
>>> TextTableFormatter.__module__
'structly.tableformat.formats.text'
>>> TextTableFormatter.__module__.split('.')[-1]
'text'
>>>
```

辞書と `__init_subclass__()` メソッドを追加することで、`TableFormatter` 基底クラスを変更します。

```python
class TableFormatter(ABC):
    _formats = { }

    @classmethod
    def __init_subclass__(cls):
        name = cls.__module__.split('.')[-1]
        TableFormatter._formats[name] = cls

    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass
```

これにより、親クラスがそのすべてのサブクラスを追跡するようになります。確認してみましょう。

```python
>>> from structly.tableformat.formatter import TableFormatter
>>> TableFormatter._formats
{'text': <class'structly.tableformat.formats.text.TextTableFormatter'>,
 'csv': <class'structly.tableformat.formats.csv.CSVTableFormatter'>,
 'html': <class'structly.tableformat.formats.html.HTMLTableFormatter'>}
>>>
```

代わりにこの辞書からクラスを検索するように、`create_formatter()` 関数を変更します。

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    formatter_cls = TableFormatter._formats.get(name)
    if not formatter_cls:
        raise RuntimeError('Unknown format %s' % name)

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
              formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()
```

`stock.py` プログラムを実行します。これらの変更を行った後も、まだ機能することを確認してください。ただ一言ですが、すべてのインポート文はまだあります。主にコードを少し整理し、ハードコードされたクラス名を削除しただけです。
