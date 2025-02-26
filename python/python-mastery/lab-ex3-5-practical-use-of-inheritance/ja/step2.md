# 汎用フォーマッタクラスの定義

`tableformat.py` ファイルに以下のクラス定義を追加します。

```python
class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()
```

次に、`print_table()` 関数を変更して、`TableFormatter` インスタンスを受け取り、出力を生成するためにそのメソッドを呼び出すようにします。

```python
def print_table(records, fields, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)
```

これらの 2 つのクラスは一緒に使うことを想定しています。たとえば：

```python
>>> import stock, reader, tableformat
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> formatter = tableformat.TableFormatter()
>>> tableformat.print_table(portfolio, ['name','shares', 'price'], formatter)
Traceback (most recent call last):
...
NotImplementedError
>>>
```

今のところ、あまり面白いことはしません。次のセクションでこれを修正します。
