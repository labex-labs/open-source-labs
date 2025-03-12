# 具体的なフォーマッタの実装

抽象基底クラスを定義し、`print_table()` 関数を更新したので、次は具体的なフォーマッタクラスを作成する時です。具体的なフォーマッタクラスとは、抽象基底クラスで定義されたメソッドの実際の実装を提供するクラスです。今回は、データをプレーンテキストの表に整形できるクラスを作成します。

`tableformat.py` ファイルに次のクラスを追加しましょう。このクラスは `TableFormatter` 抽象基底クラスを継承し、`headings()` と `row()` メソッドを実装します。

```python
class TextTableFormatter(TableFormatter):
    """
    Formatter that generates a plain - text table.
    """
    def headings(self, headers):
        """
        Generate plain - text table headings.
        """
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        """
        Generate a plain - text table row.
        """
        print(' '.join('%10s' % d for d in rowdata))
```

`TextTableFormatter` クラスは `TableFormatter` を継承しています。これは、`TableFormatter` クラスのすべてのプロパティとメソッドを取得すると同時に、`headings()` と `row()` メソッドに独自の実装を提供することを意味します。これらのメソッドは、それぞれ表のヘッダーと行を整形する役割を担っています。`headings()` メソッドは、ヘッダーをきれいに整形して出力し、その後にヘッダーとデータを区切るダッシュの行を出力します。`row()` メソッドは、各データ行を同様の方法で整形します。

では、新しいフォーマッタをテストしてみましょう。`stock`、`reader`、`tableformat` モジュールを使用して、CSV ファイルからデータを読み取り、新しいフォーマッタを使って出力します。

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.TextTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

このコードを実行すると、以前と同じ出力が表示されるはずです。これは、新しいフォーマッタが元の `print_table()` 関数と同じプレーンテキストの表を生成するように設計されているからです。

```
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

この出力は、`TextTableFormatter` が正しく動作していることを確認します。このアプローチを使用する利点は、コードをよりモジュール化し、拡張可能にしたことです。整形ロジックを別のクラス階層に分離することで、新しい出力形式を簡単に追加できます。必要なのは、`print_table()` 関数を変更することなく、`TableFormatter` の新しいサブクラスを作成するだけです。このようにして、将来的に CSV や HTML などの異なる出力形式をサポートすることができます。
