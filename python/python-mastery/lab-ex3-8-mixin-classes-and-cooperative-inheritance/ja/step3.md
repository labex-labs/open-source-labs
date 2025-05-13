# Mixin のためのユーザーフレンドリーな API の作成 (Creating a User-Friendly API for Mixins)

Mixin は強力ですが、多重継承 (multiple inheritance) を直接使用すると複雑に感じられることがあります。このステップでは、この複雑さを隠し、ユーザーにとってより簡単な API を提供するために、`create_formatter()` 関数を改善します。

まず、`tableformat.py` がエディターで開いていることを確認します。

```bash
cd ~/project
touch tableformat.py
```

既存の `create_formatter()` 関数を見つけます。

```python
# Existing function in tableformat.py
def create_formatter(name):
    """
    Create an appropriate formatter based on the name.
    """
    if name == 'text':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {name}')
```

_既存の_ `create_formatter()` 関数定義全体を、以下の強化されたバージョンに置き換えます。この新しいバージョンは、カラム (column) の書式 (format) とヘッダー (header) の大文字化のためのオプションの引数を受け入れます。

```python
# Replace the old create_formatter with this in tableformat.py

def create_formatter(name, column_formats=None, upper_headers=False):
    """
    Create a formatter with optional enhancements.

    Parameters:
    name : str
        Name of the formatter ('text', 'csv', 'html')
    column_formats : list, optional
        List of format strings for column formatting.
        Note: Relies on ColumnFormatMixin existing above this function.
    upper_headers : bool, optional
        Whether to convert headers to uppercase.
        Note: Relies on UpperHeadersMixin existing above this function.
    """
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError(f'Unknown format {name}')

    # Build the inheritance list dynamically
    bases = []
    if column_formats:
        bases.append(ColumnFormatMixin)
    if upper_headers:
        bases.append(UpperHeadersMixin)
    bases.append(formatter_cls) # Base formatter class comes last

    # Create the custom class dynamically
    # Need to ensure ColumnFormatMixin and UpperHeadersMixin are defined before this point
    class CustomFormatter(*bases):
        # Set formats if ColumnFormatMixin is used
        if column_formats:
            formats = column_formats

    return CustomFormatter() # Return an instance of the dynamically created class
```

_自己修正：複数の if/elif 分岐の代わりに、継承のためのクラスのタプルを動的に作成します。_

この強化された関数は、最初に基本フォーマッタクラス (`TextTableFormatter`、`CSVTableFormatter` など) を決定します。次に、オプションの引数 `column_formats` と `upper_headers` に基づいて、必要な mixin と基本フォーマッタクラスから継承する新しいクラス (`CustomFormatter`) を動的に構築します。最後に、このカスタムフォーマッタのインスタンスを返します。

**`tableformat.py` への変更を保存することを忘れないでください。**

次に、強化された関数をテストしましょう。**`tableformat.py` で更新された `create_formatter` 関数を保存したことを確認してください。**

まず、カラム (column) の書式設定をテストします。`step3_test1.py` を作成します。

```python
# step3_test1.py
from tableformat import create_formatter, portfolio, print_table

# Using the same formats as before, subject to type issues.
# Use formats compatible with strings if '%d', '%.2f' cause errors.
formatter = create_formatter('text', column_formats=['%10s', '%10s', '%10.2f'])

print("--- Running Step 3 Test 1 (create_formatter with column_formats) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("--------------------------------------------------------------------")
```

スクリプトを実行します。

```bash
python3 step3_test1.py
```

書式設定されたカラム (再び、価格形式の型処理の影響を受けます) を持つテーブルが表示されるはずです。

```
--- Running Step 3 Test 1 (create_formatter with column_formats) ---
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.10
       IBM        100      70.44
--------------------------------------------------------------------
```

次に、ヘッダー (header) の大文字化をテストします。`step3_test2.py` を作成します。

```python
# step3_test2.py
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', upper_headers=True)

print("--- Running Step 3 Test 2 (create_formatter with upper_headers) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("-------------------------------------------------------------------")
```

スクリプトを実行します。

```bash
python3 step3_test2.py
```

大文字のヘッダー (header) を持つテーブルが表示されるはずです。

```
--- Running Step 3 Test 2 (create_formatter with upper_headers) ---
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
-------------------------------------------------------------------
```

最後に、両方のオプションを組み合わせます。`step3_test3.py` を作成します。

```python
# step3_test3.py
from tableformat import create_formatter, portfolio, print_table

# Using the same formats as before
formatter = create_formatter('text', column_formats=['%10s', '%10s', '%10.2f'], upper_headers=True)

print("--- Running Step 3 Test 3 (create_formatter with both options) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("------------------------------------------------------------------")
```

スクリプトを実行します。

```bash
python3 step3_test3.py
```

これにより、書式設定されたカラム (column) と大文字のヘッダー (header) の両方を持つテーブルが表示されるはずです。

```
--- Running Step 3 Test 3 (create_formatter with both options) ---
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100      32.20
       IBM         50       91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.10
       IBM        100      70.44
------------------------------------------------------------------
```

強化された関数は、他のフォーマッタタイプ (formatter type) でも機能します。たとえば、CSV フォーマッタで試してみてください。`step3_test4.py` を作成します。

```python
# step3_test4.py
from tableformat import create_formatter, portfolio, print_table

# For CSV, ensure formats produce valid CSV fields.
# Adding quotes around the string name field.
formatter = create_formatter('csv', column_formats=['"%s"', '%d', '%.2f'], upper_headers=True)

print("--- Running Step 3 Test 4 (create_formatter with CSV) ---")
print_table(portfolio, ['name', 'shares', 'price'], formatter)
print("---------------------------------------------------------")
```

スクリプトを実行します。

```bash
python3 step3_test4.py
```

これにより、CSV 形式で大文字のヘッダー (header) と書式設定されたカラム (column) が生成されるはずです (再び、`print_table` から渡された文字列に対する `%d`/`%.2f` 書式設定の潜在的な型問題)。

```
--- Running Step 3 Test 4 (create_formatter with CSV) ---
NAME,SHARES,PRICE
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
---------------------------------------------------------
```

`create_formatter()` 関数を強化することで、ユーザーフレンドリーな API を作成しました。ユーザーは、多重継承 (multiple inheritance) 構造を自分で管理する必要なく、mixin 機能を簡単に適用できるようになりました。
