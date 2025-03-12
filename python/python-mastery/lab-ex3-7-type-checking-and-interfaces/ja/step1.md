# print_table() への型チェックの追加

このステップでは、`tableformat.py` ファイル内の `print_table()` 関数を改善します。`formatter` パラメータが有効な `TableFormatter` インスタンスであるかどうかをチェックする機能を追加します。なぜこれが必要なのでしょうか？型チェックは、コードの安全ネットのようなものです。取り扱うデータが正しい型であることを確認し、見つけにくいバグを防ぐのに役立ちます。

## Python での型チェックの理解

型チェックは、プログラミングにおいて非常に有用なテクニックです。開発プロセスの早い段階でエラーを検出することができます。Python では、さまざまな型のオブジェクトを扱うことが多く、関数に特定の型のオブジェクトが渡されることを期待することがあります。オブジェクトが特定の型またはそのサブクラスであるかどうかをチェックするには、`isinstance()` 関数を使用できます。たとえば、リストを期待する関数がある場合、`isinstance()` を使用して入力が実際にリストであることを確認できます。

## print_table() 関数の修正

まず、コードエディタで `tableformat.py` ファイルを開きます。ファイルの末尾までスクロールすると、`print_table()` 関数が見つかります。最初は次のようになっています。

```python
def print_table(data, columns, formatter):
    '''
    Print a table showing selected columns from a data source
    using the given formatter.
    '''
    formatter.headings(columns)
    for item in data:
        rowdata = [str(getattr(item, col)) for col in columns]
        formatter.row(rowdata)
```

この関数は、いくつかのデータ、列のリスト、およびフォーマッタを受け取ります。そして、フォーマッタを使用してテーブルを印刷します。ただし、現時点ではフォーマッタが正しい型であるかどうかをチェックしていません。

型チェックを追加するために修正しましょう。`isinstance()` 関数を使用して、`formatter` パラメータが `TableFormatter` のインスタンスであるかどうかをチェックします。もしそうでなければ、明確なメッセージを含む `TypeError` を発生させます。修正後のコードは次のとおりです。

```python
def print_table(data, columns, formatter):
    '''
    Print a table showing selected columns from a data source
    using the given formatter.
    '''
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")

    formatter.headings(columns)
    for item in data:
        rowdata = [str(getattr(item, col)) for col in columns]
        formatter.row(rowdata)
```

## 型チェック実装のテスト

型チェックを追加したので、それが機能することを確認する必要があります。`test_tableformat.py` という新しい Python ファイルを作成しましょう。以下のコードを記述します。

```python
import stock
import reader
import tableformat

# Read portfolio data
portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)

# Define a formatter that doesn't inherit from TableFormatter
class MyFormatter:
    def headings(self, headers):
        pass
    def row(self, rowdata):
        pass

# Try to use the non-compliant formatter
try:
    tableformat.print_table(portfolio, ['name', 'shares', 'price'], MyFormatter())
    print("Test failed - type checking not implemented")
except TypeError as e:
    print(f"Test passed - caught error: {e}")
```

このコードでは、まずポートフォリオデータを読み込みます。次に、`TableFormatter` を継承していない新しいフォーマッタクラス `MyFormatter` を定義します。この非互換のフォーマッタを `print_table()` 関数で使用しようとします。型チェックが機能していれば、`TypeError` が発生するはずです。

テストを実行するには、ターミナルを開き、`test_tableformat.py` ファイルがあるディレクトリに移動します。次のコマンドを実行します。

```bash
python test_tableformat.py
```

すべてが正しく動作していれば、次のような出力が表示されます。

```
Test passed - caught error: Expected a TableFormatter
```

この出力は、型チェックが期待どおりに機能していることを確認します。これで、`print_table()` 関数は `TableFormatter` のインスタンスまたはそのサブクラスであるフォーマッタのみを受け入れるようになりました。
