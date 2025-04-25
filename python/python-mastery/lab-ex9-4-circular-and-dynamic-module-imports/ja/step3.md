# サブクラス登録の実装

プログラミングにおいて、循環インポート（Circular imports）は厄介な問題になります。フォーマッタークラスを直接インポートする代わりに、登録パターンを使用することができます。このパターンでは、サブクラスが自身を親クラスに登録します。これは循環インポートを回避するための一般的で効果的な方法です。

まず、クラスのモジュール名を調べる方法を理解しましょう。モジュール名は、登録パターンで使用するため重要です。これを行うために、ターミナルで Python コマンドを実行します。

```bash
cd ~/project/structly
python3 -c "from structly.tableformat.formats.text import TextTableFormatter; print(TextTableFormatter.__module__); print(TextTableFormatter.__module__.split('.')[-1])"
```

このコマンドを実行すると、次のような出力が表示されます。

```
structly.tableformat.formats.text
text
```

この出力は、クラス自体からモジュール名を抽出できることを示しています。後でこのモジュール名を使用してサブクラスを登録します。

次に、`tableformat/formatter.py`ファイルの`TableFormatter`クラスを変更して、登録メカニズムを追加しましょう。WebIDE でこのファイルを開きます。`TableFormatter`クラスにいくつかのコードを追加します。このコードは、サブクラスを自動的に登録するのに役立ちます。

```python
class TableFormatter(ABC):
    _formats = { }  # Dictionary to store registered formatters

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

`__init_subclass__`メソッドは Python の特殊メソッドです。`TableFormatter`のサブクラスが作成されるたびに呼び出されます。このメソッドでは、サブクラスのモジュール名を抽出し、それをキーとして`_formats`辞書にサブクラスを登録します。

次に、登録辞書を使用するように`create_formatter`関数を変更する必要があります。この関数は、指定された名前に基づいて適切なフォーマッターを作成する役割を持っています。

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

これらの変更を加えた後、ファイルを保存します。次に、プログラムが引き続き動作するかどうかをテストしましょう。`stock.py`スクリプトを実行します。

```bash
python3 stock.py
```

プログラムが正常に実行されれば、変更によって何かが壊れていないことを意味します。次に、登録がどのように機能するかを確認するために、`_formats`辞書の内容を見てみましょう。

```bash
python3 -c "from structly.tableformat.formatter import TableFormatter; print(TableFormatter._formats)"
```

次のような出力が表示されるはずです。

```
{'text': <class 'structly.tableformat.formats.text.TextTableFormatter'>, 'csv': <class 'structly.tableformat.formats.csv.CSVTableFormatter'>, 'html': <class 'structly.tableformat.formats.html.HTMLTableFormatter'>}
```

この出力は、サブクラスが`_formats`辞書に正しく登録されていることを確認しています。ただし、ファイルの途中にまだいくつかのインポート文があります。次のステップでは、動的インポート（Dynamic imports）を使用してこの問題を解決します。
