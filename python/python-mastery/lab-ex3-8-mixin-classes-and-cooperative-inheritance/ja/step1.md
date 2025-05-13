# カラム (Column) の書式設定における問題の理解 (Understanding the Problem with Column Formatting)

このステップでは、現在のテーブル書式設定の実装における制限事項について見ていきます。また、この問題に対するいくつかの可能な解決策を検討します。

まず、何をするのかを理解しましょう。VSCode エディターを開き、プロジェクトディレクトリにある `tableformat.py` ファイルを見てみます。このファイルは、テーブル形式のデータをテキスト、CSV、HTML などのさまざまな形式で書式設定できるようにするコードが含まれているため、重要です。

ファイルを開くには、ターミナルで次のコマンドを使用します。`cd` コマンドはディレクトリをプロジェクトディレクトリに変更し、`code` コマンドは VSCode で `tableformat.py` ファイルを開きます。

```bash
cd ~/project
touch tableformat.py
```

ファイルを開くと、いくつかのクラスが定義されていることに気付くでしょう。これらのクラスは、テーブルデータの書式設定において異なる役割を果たします。

- `TableFormatter`: これは抽象基底クラス (abstract base class) です。テーブルの見出しと行を書式設定するために使用されるメソッドがあります。他のフォーマッタクラスの設計図と考えてください。
- `TextTableFormatter`: このクラスは、テーブルをプレーンテキスト形式で出力するために使用されます。
- `CSVTableFormatter`: これは、テーブルデータを CSV (Comma-Separated Values) 形式で書式設定する役割を担います。
- `HTMLTableFormatter`: このクラスは、テーブルデータを HTML 形式で書式設定します。

ファイルには `print_table()` 関数もあります。この関数は、先ほど説明したフォーマッタクラスを使用して、テーブル形式のデータを表示します。

次に、これらのクラスがどのように機能するかを見てみましょう。`/home/labex/project` ディレクトリに、エディターまたは `touch` コマンドを使用して `step1_test1.py` という名前の新しいファイルを作成します。次の Python コードを追加します。

```python
# step1_test1.py
from tableformat import print_table, TextTableFormatter, portfolio

formatter = TextTableFormatter()
print("--- Running Step 1 Test 1 ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("-----------------------------")
```

ファイルを保存し、ターミナルから実行します。

```bash
python3 step1_test1.py
```

スクリプトを実行すると、次のような出力が表示されるはずです。

```
--- Running Step 1 Test 1 ---
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
-----------------------------
```

次に、問題を見つけましょう。`price` カラム (column) の値の書式が統一されていないことに注意してください。32.2 のように小数点以下 1 桁の値もあれば、51.23 のように小数点以下 2 桁の値もあります。金融データでは、通常、書式設定は一貫していることが望ましいです。

出力は次のようになっていることが望ましいです。

```
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

これを修正する 1 つの方法は、書式指定 (format specifications) を受け入れるように `print_table()` 関数を変更することです。`tableformat.py` を実際に変更せずに、これがどのように機能するかを見てみましょう。次の内容で `step1_test2.py` という名前の新しいファイルを作成します。このスクリプトは、デモンストレーションのために `print_table` 関数をローカルで再定義します。

```python
# step1_test2.py
from tableformat import TextTableFormatter

# Re-define Stock and portfolio locally for this example
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

portfolio = [
    Stock('AA', 100, 32.20), Stock('IBM', 50, 91.10), Stock('CAT', 150, 83.44),
    Stock('MSFT', 200, 51.23), Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.10),
    Stock('IBM', 100, 70.44)
]

# Define a modified print_table locally
def print_table_modified(records, fields, formats, formatter):
    formatter.headings(fields)
    for r in records:
        # Apply formats to the original attribute values
        rowdata = [(fmt % getattr(r, fieldname))
                   for fieldname, fmt in zip(fields, formats)]
        # Pass the already formatted strings to the formatter's row method
        formatter.row(rowdata)

print("--- Running Step 1 Test 2 ---")
formatter = TextTableFormatter()
# Note: TextTableFormatter.row expects strings already formatted for width.
# This example might not align perfectly yet, but demonstrates passing formats.
print_table_modified(portfolio,
                     ['name', 'shares', 'price'],
                     ['%10s', '%10d', '%10.2f'], # Using widths
                     formatter)
print("-----------------------------")

```

このスクリプトを実行します。

```bash
python3 step1_test2.py
```

このアプローチは書式 (format) を渡すことを示していますが、`print_table` を変更することには欠点があります。関数のインターフェース (interface) を変更すると、元のバージョンを使用する既存のコードが壊れる可能性があります。

別のアプローチは、サブクラス化 (subclassing) によってカスタムフォーマッタ (custom formatter) を作成することです。`TextTableFormatter` から継承し、`row()` メソッド (method) をオーバーライド (override) する新しいクラスを作成できます。`step1_test3.py` ファイルを作成します。

```python
# step1_test3.py
from tableformat import TextTableFormatter, print_table, portfolio

class PortfolioFormatter(TextTableFormatter):
    def row(self, rowdata):
        # Example: Add a prefix to demonstrate overriding
        # Note: The original lab description's formatting example had data type issues
        # because print_table sends strings to this method. This is a simpler demo.
        print("> ", end="") # Add a simple prefix to the line start
        super().row(rowdata) # Call the parent method

print("--- Running Step 1 Test 3 ---")
formatter = PortfolioFormatter()
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("-----------------------------")
```

スクリプトを実行します。

```bash
python3 step1_test3.py
```

この解決策はサブクラス化を示すのに役立ちますが、書式設定のバリエーションごとに新しいクラスを作成するのは不便です。さらに、継承元の基底クラス (ここでは `TextTableFormatter`) に縛られます。

次のステップでは、mixin クラスを使用した、よりエレガントな解決策を探ります。
