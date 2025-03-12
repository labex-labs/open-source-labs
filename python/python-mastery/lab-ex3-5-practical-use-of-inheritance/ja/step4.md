# 追加のフォーマッタの作成

プログラミングにおいて、継承は既存のクラスを基に新しいクラスを作成することができる強力な概念です。これによりコードの再利用が可能になり、プログラムをより拡張性の高いものにすることができます。この実験のこの部分では、継承を使って、異なる出力形式（CSV と HTML）用の 2 つの新しいフォーマッタを作成します。これらのフォーマッタは基底クラスを継承するため、共通の振る舞いを共有しながら、独自のデータ整形方法を持つことになります。

では、`tableformat.py` ファイルに次のクラスを追加しましょう。これらのクラスは、それぞれ CSV 形式と HTML 形式でデータを整形する方法を定義します。

```python
class CSVTableFormatter(TableFormatter):
    """
    Formatter that generates CSV formatted data.
    """
    def headings(self, headers):
        """
        Generate CSV headers.
        """
        print(','.join(headers))

    def row(self, rowdata):
        """
        Generate a CSV data row.
        """
        print(','.join(str(d) for d in rowdata))

class HTMLTableFormatter(TableFormatter):
    """
    Formatter that generates HTML table code.
    """
    def headings(self, headers):
        """
        Generate HTML table headers.
        """
        print('<tr>', end=' ')
        for header in headers:
            print(f'<th>{header}</th>', end=' ')
        print('</tr>')

    def row(self, rowdata):
        """
        Generate an HTML table row.
        """
        print('<tr>', end=' ')
        for data in rowdata:
            print(f'<td>{data}</td>', end=' ')
        print('</tr>')
```

`CSVTableFormatter` クラスは、データを CSV（Comma-Separated Values、カンマ区切り値）形式で整形するように設計されています。`headings` メソッドはヘッダーのリストを受け取り、それらをカンマで区切って出力します。`row` メソッドは 1 行分のデータのリストを受け取り、同様にカンマで区切って出力します。

一方、`HTMLTableFormatter` クラスは HTML の表コードを生成するために使用されます。`headings` メソッドは HTML の `<th>` タグを使って表のヘッダーを作成し、`row` メソッドは HTML の `<td>` タグを使って表の行を作成します。

これらの新しいフォーマッタがどのように動作するかをテストしてみましょう。

1. まず、CSV フォーマッタをテストしましょう。

```python
import stock
import reader
import tableformat

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
formatter = tableformat.CSVTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

このコードでは、まず必要なモジュールをインポートします。次に、`portfolio.csv` という名前の CSV ファイルからデータを読み取り、`Stock` クラスのインスタンスを作成します。その後、`CSVTableFormatter` クラスのインスタンスを作成します。最後に、`print_table` 関数を使ってポートフォリオデータを CSV 形式で出力します。

次のような CSV 形式の出力が表示されるはずです。

```
name,shares,price
AA,100,32.2
IBM,50,91.1
CAT,150,83.44
MSFT,200,51.23
GE,95,40.37
MSFT,50,65.1
IBM,100,70.44
```

2. 次に、HTML フォーマッタをテストしましょう。

```python
formatter = tableformat.HTMLTableFormatter()
tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

ここでは、`HTMLTableFormatter` クラスのインスタンスを作成し、再び `print_table` 関数を使ってポートフォリオデータを HTML 形式で出力します。

次のような HTML 形式の出力が表示されるはずです。

```
<tr> <th>name</th> <th>shares</th> <th>price</th> </tr>
<tr> <td>AA</td> <td>100</td> <td>32.2</td> </tr>
<tr> <td>IBM</td> <td>50</td> <td>91.1</td> </tr>
<tr> <td>CAT</td> <td>150</td> <td>83.44</td> </tr>
<tr> <td>MSFT</td> <td>200</td> <td>51.23</td> </tr>
<tr> <td>GE</td> <td>95</td> <td>40.37</td> </tr>
<tr> <td>MSFT</td> <td>50</td> <td>65.1</td> </tr>
<tr> <td>IBM</td> <td>100</td> <td>70.44</td> </tr>
```

ご覧の通り、各フォーマッタは異なる形式の出力を生成しますが、すべて `TableFormatter` 基底クラスで定義された同じインターフェースを共有しています。これは、継承と多態性の力を示す素晴らしい例です。基底クラスを使ってコードを書くことができ、それは自動的に任意のサブクラスで動作します。

`print_table()` 関数は、使用される具体的なフォーマッタについて何も知る必要はありません。基底クラスで定義されたメソッドを呼び出すだけで、提供されたフォーマッタのタイプに基づいて適切な実装が選択されます。これにより、コードがより柔軟になり、保守が容易になります。
