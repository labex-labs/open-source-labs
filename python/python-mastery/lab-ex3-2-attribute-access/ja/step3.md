# 属性アクセスを使用したテーブルフォーマッタの作成

プログラミングにおいて、属性アクセスはオブジェクトのプロパティとやり取りするための基本的な概念です。今回は、属性アクセスについて学んだことを実践に移します。便利なユーティリティであるテーブルフォーマッタを作成します。このフォーマッタはオブジェクトのコレクションを受け取り、それを表形式で表示します。これにより、データが読みやすく理解しやすくなります。

## tableformat.py モジュールの作成

まず、新しいPythonファイルを作成する必要があります。このファイルには、テーブルフォーマッタのコードが格納されます。

ファイルを作成するには、以下の手順に従います。

1. WebIDEで「File」メニューをクリックします。
2. ドロップダウンメニューから「New File」を選択します。
3. 新しく作成したファイルを `/home/labex/project/` ディレクトリに `tableformat.py` として保存します。

ファイルができたので、`tableformat.py` の中に `print_table()` 関数のコードを書きましょう。この関数は、オブジェクトを表形式で整形して表示する役割を担います。

```python
def print_table(objects, fields):
    """
    Print a collection of objects as a formatted table.

    Args:
        objects: A sequence of objects
        fields: A list of attribute names
    """
    # Print the header
    headers = fields
    for header in headers:
        print(f"{header:>10}", end=' ')
    print()

    # Print the separator line
    for header in headers:
        print("-" * 10, end=' ')
    print()

    # Print the data
    for obj in objects:
        for field in fields:
            value = getattr(obj, field)
            print(f"{value:>10}", end=' ')
        print()
```

この関数が行うことを分解してみましょう。

1. 2つの引数を受け取ります。オブジェクトのシーケンスと属性名のリストです。オブジェクトのシーケンスは表示したいデータで、属性名のリストはオブジェクトのどのプロパティを表示するかを関数に伝えます。
2. ヘッダー行を表示します。ヘッダー行には、表示したい属性の名前が含まれます。
3. 区切り線を表示します。この線は、ヘッダーとデータを視覚的に区切るのに役立ちます。
4. シーケンス内の各オブジェクトについて、指定された各属性の値を表示します。各オブジェクトの属性値にアクセスするために `getattr()` 関数を使用します。

では、`print_table()` 関数が期待通りに動作するかテストしてみましょう。

```python
# Open a Python interactive shell
python3

# Import our modules
from stock import read_portfolio
import tableformat

# Read the portfolio data
portfolio = read_portfolio('portfolio.csv')

# Print the portfolio as a table with name, shares, and price columns
tableformat.print_table(portfolio, ['name', 'shares', 'price'])
```

上記のコードを実行すると、以下の出力が表示されるはずです。

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

`print_table()` 関数の素晴らしい点の1つは、その柔軟性です。`fields` リストを変更するだけで、表示する列を変更することができます。

```python
# Just show shares and name
tableformat.print_table(portfolio, ['shares', 'name'])
```

このコードを実行すると、以下の出力が得られます。

```
    shares       name
---------- ----------
       100         AA
        50        IBM
       150        CAT
       200       MSFT
        95         GE
        50       MSFT
       100        IBM
```

このアプローチの強みは、その汎用性にあります。表示したい属性の名前がわかっていれば、同じ `print_table()` 関数を使用して、あらゆる種類のオブジェクトの表を表示することができます。これにより、テーブルフォーマッタはプログラミングツールキットの中で非常に便利なツールになります。
