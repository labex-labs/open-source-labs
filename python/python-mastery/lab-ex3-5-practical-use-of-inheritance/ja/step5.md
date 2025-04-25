# ファクトリ関数の作成

継承を使用する際の一般的なチャレンジの 1 つは、ユーザーが具体的なフォーマッタクラスの名前を覚えておく必要があることです。特にクラスの数が増えると、これはかなり面倒なことになります。このプロセスを簡素化するために、ファクトリ関数を作成することができます。ファクトリ関数は、オブジェクトを作成して返す特殊なタイプの関数です。今回の場合、単純な形式名に基づいて適切なフォーマッタを返します。

`tableformat.py` ファイルに次の関数を追加しましょう。この関数は形式名を引数として受け取り、対応するフォーマッタオブジェクトを返します。

```python
def create_formatter(format_name):
    """
    Create a formatter of the specified type.

    Args:
        format_name: Name of the formatter ('text', 'csv', 'html')

    Returns:
        A TableFormatter object

    Raises:
        ValueError: If format_name is not recognized
    """
    if format_name == 'text':
        return TextTableFormatter()
    elif format_name == 'csv':
        return CSVTableFormatter()
    elif format_name == 'html':
        return HTMLTableFormatter()
    else:
        raise ValueError(f'Unknown format {format_name}')
```

`create_formatter()` 関数はファクトリ関数です。この関数は、あなたが提供する `format_name` 引数をチェックします。もしそれが 'text' なら、`TextTableFormatter` オブジェクトを作成して返します。'csv' なら、`CSVTableFormatter` オブジェクトを返し、'html' なら、`HTMLTableFormatter` オブジェクトを返します。形式名が認識されない場合は、`ValueError` を発生させます。このようにして、ユーザーは具体的なクラス名を知らなくても、単純な名前を提供するだけで簡単にフォーマッタを選択できます。

では、ファクトリ関数をテストしてみましょう。既存のいくつかの関数とクラスを使用して、CSV ファイルからデータを読み取り、異なる形式で出力します。

```python
import stock
import reader
from tableformat import create_formatter, print_table

portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)

# Test with text formatter
formatter = create_formatter('text')
print("\nText Format:")
print_table(portfolio, ['name', 'shares', 'price'], formatter)

# Test with CSV formatter
formatter = create_formatter('csv')
print("\nCSV Format:")
print_table(portfolio, ['name', 'shares', 'price'], formatter)

# Test with HTML formatter
formatter = create_formatter('html')
print("\nHTML Format:")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
```

このコードでは、まず必要なモジュールと関数をインポートします。次に、`portfolio.csv` ファイルからデータを読み取り、`portfolio` オブジェクトを作成します。その後、'text'、'csv'、'html' という異なる形式名で `create_formatter()` 関数をテストします。各形式について、フォーマッタオブジェクトを作成し、形式名を出力し、そして `print_table()` 関数を使用して `portfolio` データを指定された形式で出力します。

このコードを実行すると、形式名で区切られた 3 つの形式の出力が表示されるはずです。

```
Text Format:
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44

CSV Format:
name,shares,price
AA,100,32.2
IBM,50,91.1
CAT,150,83.44
MSFT,200,51.23
GE,95,40.37
MSFT,50,65.1
IBM,100,70.44

HTML Format:
<tr> <th>name</th> <th>shares</th> <th>price</th> </tr>
<tr> <td>AA</td> <td>100</td> <td>32.2</td> </tr>
<tr> <td>IBM</td> <td>50</td> <td>91.1</td> </tr>
<tr> <td>CAT</td> <td>150</td> <td>83.44</td> </tr>
<tr> <td>MSFT</td> <td>200</td> <td>51.23</td> </tr>
<tr> <td>GE</td> <td>95</td> <td>40.37</td> </tr>
<tr> <td>MSFT</td> <td>50</td> <td>65.1</td> </tr>
<tr> <td>IBM</td> <td>100</td> <td>70.44</td> </tr>
```

ファクトリ関数は、クラスのインスタンス化の詳細を隠すため、コードをより使いやすくします。ユーザーはフォーマッタオブジェクトを作成する方法を知る必要はなく、欲しい形式を指定するだけで済みます。

オブジェクトを作成するためにファクトリ関数を使用するこのパターンは、オブジェクト指向プログラミングにおける一般的なデザインパターンで、ファクトリパターンとして知られています。これは、クライアントコード（フォーマッタを使用するコード）と実際の実装クラス（フォーマッタクラス）の間に抽象化のレイヤーを提供します。これにより、コードがよりモジュール化され、使いやすくなります。

**重要概念の復習：**

1. **抽象基底クラス**: `TableFormatter` クラスはインターフェースとして機能します。インターフェースは、それを実装するすべてのクラスが持たなければならないメソッドのセットを定義します。今回の場合、すべてのフォーマッタクラスは `TableFormatter` クラスで定義されたメソッドを実装しなければなりません。

2. **継承**: `TextTableFormatter`、`CSVTableFormatter`、`HTMLTableFormatter` のような具体的なフォーマッタクラスは、基底の `TableFormatter` クラスを継承しています。これは、基底クラスから基本的な構造とメソッドを取得し、独自の具体的な実装を提供できることを意味します。

3. **多態性**: `print_table()` 関数は、必要なインターフェースを実装する任意のフォーマッタで動作することができます。これは、異なるフォーマッタオブジェクトを `print_table()` 関数に渡すことができ、それぞれで正しく動作することを意味します。

4. **ファクトリパターン**: `create_formatter()` 関数は、フォーマッタオブジェクトの作成を簡素化します。形式名に基づいて適切なオブジェクトを作成する詳細を処理するため、ユーザーはそれについて心配する必要がありません。

これらのオブジェクト指向の原則を使用することで、様々な出力形式で表形式のデータを整形するための柔軟で拡張可能なシステムを作成しました。
