# 基底クラスの作成と print 関数の修正

プログラミングにおいて、継承はクラスの階層を作成することができる強力な概念です。異なる形式でデータを出力するために継承を利用するには、まず基底クラスを作成する必要があります。基底クラスは他のクラスの青写真となり、サブクラスが継承したりオーバーライドしたりできる共通のメソッドセットを定義します。

では、すべての表フォーマッタのインターフェースを定義する基底クラスを作成しましょう。WebIDE で `tableformat.py` ファイルを開き、ファイルの先頭に次のコードを追加します。

```python
class TableFormatter:
    """
    Base class for all table formatters.
    This class defines the interface that all formatters must implement.
    """
    def headings(self, headers):
        """
        Generate the table headings.
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Generate a single row of table data.
        """
        raise NotImplementedError()
```

`TableFormatter` クラスは抽象基底クラスです。抽象基底クラスはメソッドを定義するが、それらの実装を提供しないクラスです。代わりに、サブクラスがこれらの実装を提供することを期待しています。`NotImplementedError` 例外は、これらのメソッドがサブクラスによってオーバーライドされなければならないことを示すために使用されます。サブクラスがこれらのメソッドをオーバーライドせずに使用しようとすると、エラーが発生します。

次に、`print_table()` 関数を修正して `TableFormatter` クラスを使用するようにします。`print_table()` 関数は、オブジェクトのリストからデータの表を出力するために使用されます。これを修正して `TableFormatter` クラスを使用することで、関数をより柔軟にし、異なる表形式で動作できるようにすることができます。

既存の `print_table()` 関数を次のコードに置き換えます。

```python
def print_table(records, fields, formatter):
    """
    Print a table of data from a list of objects using the specified formatter.

    Args:
        records: A list of objects
        fields: A list of field names
        formatter: A TableFormatter object
    """
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)
```

ここでの重要な変更点は、`print_table()` が現在 `formatter` パラメータを受け取るようになったことです。このパラメータは `TableFormatter` のインスタンスまたはサブクラスである必要があります。これは、異なる表フォーマッタを `print_table()` 関数に渡すことができ、適切なフォーマッタを使用して表を出力できることを意味します。関数は、`headings()` および `row()` メソッドを呼び出すことで、フォーマットの責任をフォーマッタオブジェクトに委譲します。

基底の `TableFormatter` クラスを使用して変更をテストしてみましょう。

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.TableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

このコードを実行すると、エラーが表示されるはずです。

```
Traceback (most recent call last):
...
NotImplementedError
```

このエラーが発生するのは、抽象基底クラスを直接使用しようとしているが、そのメソッドの実装が提供されていないためです。`TableFormatter` クラスの `headings()` および `row()` メソッドが `NotImplementedError` を発生させるため、これらのメソッドが呼び出されたときに Python は何をすればよいかを知りません。次のステップでは、これらの実装を提供する具体的なサブクラスを作成します。
