# ミックスイン用の使いやすい API の作成

ミックスインは Python の強力な機能ですが、多重継承を伴うため、初心者には少し扱いにくい場合があります。多重継承はかなり複雑になることがあります。このステップでは、`create_formatter()` 関数を改良することで、ユーザーにとって使いやすいものにします。これにより、ユーザーは多重継承の詳細にあまり気を使う必要がなくなります。

まず、`tableformat.py` ファイルを開く必要があります。ターミナルで以下のコマンドを実行することで、これを行うことができます。`cd` コマンドはディレクトリをプロジェクトフォルダに変更し、`code` コマンドはコードエディタで `tableformat.py` ファイルを開きます。

```bash
cd ~/project
code tableformat.py
```

ファイルが開いたら、`create_formatter()` 関数を見つけます。現在、この関数は次のようになっています。

```python
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

この関数は名前を引数として受け取り、対応するフォーマッタを返します。しかし、もっと柔軟にするために、ミックスイン用のオプション引数を受け取れるように変更します。

既存の `create_formatter()` 関数を以下の拡張版に置き換えます。この新しい関数では、列フォーマットとヘッダーを大文字に変換するかどうかを指定できます。

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    """
    Create a formatter with optional enhancements.

    Parameters:
    name : str
        Name of the formatter ('text', 'csv', 'html')
    column_formats : list, optional
        List of format strings for column formatting
    upper_headers : bool, optional
        Whether to convert headers to uppercase
    """
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError(f'Unknown format {name}')

    # Apply mixins if requested
    if column_formats and upper_headers:
        class CustomFormatter(ColumnFormatMixin, UpperHeadersMixin, formatter_cls):
            formats = column_formats
        return CustomFormatter()
    elif column_formats:
        class CustomFormatter(ColumnFormatMixin, formatter_cls):
            formats = column_formats
        return CustomFormatter()
    elif upper_headers:
        class CustomFormatter(UpperHeadersMixin, formatter_cls):
            pass
        return CustomFormatter()
    else:
        return formatter_cls()
```

この拡張された関数は、まず `name` 引数に基づいて基本のフォーマッタクラスを決定します。次に、`column_formats` と `upper_headers` が指定されているかどうかに応じて、適切なミックスインを含むカスタムフォーマッタクラスを作成します。最後に、カスタムフォーマッタクラスのインスタンスを返します。

では、さまざまなオプションの組み合わせで拡張された関数をテストしましょう。

まず、列フォーマットを使用してみましょう。ターミナルで以下のコマンドを実行します。このコマンドは、`tableformat.py` ファイルから必要な関数とデータをインポートし、列フォーマットを持つフォーマッタを作成し、そのフォーマッタを使用して表を印刷します。

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', column_formats=['%s', '%d', '%0.2f'])
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

列がフォーマットされた表が表示されるはずです。出力は次のようになります。

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

次に、大文字のヘッダーを使用してみましょう。以下のコマンドを実行します。

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', upper_headers=True)
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

大文字のヘッダーを持つ表が表示されるはずです。出力は次のようになります。

```
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

最後に、両方のオプションを組み合わせてみましょう。このコマンドを実行します。

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('text', column_formats=['%s', '%d', '%0.2f'], upper_headers=True)
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

これにより、列がフォーマットされ、ヘッダーが大文字の表が表示されるはずです。出力は次のようになります。

```
      NAME     SHARES      PRICE
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
```

拡張された関数は、他のフォーマッタタイプでも機能します。たとえば、CSV フォーマッタで試してみましょう。以下のコマンドを実行します。

```python
python3 -c "
from tableformat import create_formatter, portfolio, print_table

formatter = create_formatter('csv', column_formats=['\\"%s\\"', '%d', '%0.2f'])
print_table(portfolio, ['name', 'shares', 'price'], formatter)
"
```

これにより、列がフォーマットされた CSV 出力が生成されるはずです。出力は次のようになります。

```
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
```

`create_formatter()` 関数を拡張することで、使いやすい API を作成しました。ユーザーは今では、多重継承の複雑な詳細を理解することなく、簡単にミックスインを使用できます。これにより、ユーザーは自分のニーズに合わせてフォーマッタをカスタマイズする柔軟性が得られます。
