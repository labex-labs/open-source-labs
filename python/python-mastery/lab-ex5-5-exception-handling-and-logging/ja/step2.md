# 例外処理の実装

このステップでは、コードをより堅牢にすることに焦点を当てます。プログラムが不適切なデータに遭遇すると、しばしばクラッシュします。しかし、例外処理と呼ばれる手法を使って、これらの問題を適切に処理することができます。`reader.py` ファイルを修正してこれを実装します。例外処理により、プログラムは予期しないデータに直面しても、突然停止する代わりに実行を続けることができます。

## try-except ブロックの理解

Python は、try-except ブロックを使って例外を処理する強力な方法を提供しています。その仕組みを解説します。

```python
try:
    # Code that might cause an exception
    result = risky_operation()
except SomeExceptionType as e:
    # Code that runs if the exception occurs
    handle_exception(e)
```

`try` ブロックには、例外を引き起こす可能性のあるコードを記述します。例外とは、プログラムの実行中に発生するエラーです。たとえば、数をゼロで割ろうとすると、Python は `ZeroDivisionError` 例外を発生させます。`try` ブロック内で例外が発生すると、Python は `try` ブロック内のコードの実行を停止し、一致する `except` ブロックにジャンプします。`except` ブロックには、例外を処理するコードが含まれています。`SomeExceptionType` は、キャッチしたい例外の型です。特定の型の例外をキャッチすることも、一般的な `Exception` を使ってすべての型の例外をキャッチすることもできます。`as e` の部分で、エラーに関する情報を含む例外オブジェクトにアクセスできます。

## コードの修正

では、try-except ブロックについて学んだことを `convert_csv()` 関数に適用しましょう。エディタで `reader.py` ファイルを開きます。

1. 現在の `convert_csv()` 関数を次のコードに置き換えます。

```python
def convert_csv(rows, converter, header=True):
    """
    Convert a sequence of rows to an output sequence according to a conversion function.
    """
    if header:
        headers = next(rows)
    else:
        headers = []

    result = []
    for row_idx, row in enumerate(rows, start=1):
        try:
            # Try to convert the row
            result.append(converter(headers, row))
        except Exception as e:
            # Print a warning message for bad rows
            print(f"Row {row_idx}: Bad row: {row}")
            continue

    return result
```

この新しい実装では、以下のことを行っています。

- `map()` の代わりに `for` ループを使って各行を処理します。これにより、各行の処理をより細かく制御できます。
- 変換コードを try-except ブロックで囲みます。これは、行の変換中に例外が発生しても、プログラムがクラッシュしないことを意味します。代わりに、`except` ブロックにジャンプします。
- `except` ブロックでは、無効な行に対するエラーメッセージを出力します。これにより、どの行に問題があるかを特定できます。
- エラーメッセージを出力した後、`continue` 文を使って現在の行をスキップし、残りの行の処理を続けます。

これらの変更を加えた後、ファイルを保存します。

## 変更のテスト

修正したコードを `missing.csv` ファイルでテストしましょう。まず、ターミナルで次のコマンドを実行して Python インタープリタを開きます。

```bash
python3
```

Python インタープリタに入ったら、次のコードを実行します。

```python
from reader import read_csv_as_dicts
port = read_csv_as_dicts('missing.csv', types=[str, int, float])
print(f"Number of valid rows processed: {len(port)}")
```

このコードを実行すると、問題のある各行に対するエラーメッセージが表示されるはずです。ただし、プログラムは処理を続け、有効な行を返します。以下は、表示される可能性のある出力の例です。

```
Row 4: Bad row: ['C', '', '53.08']
Row 7: Bad row: ['DIS', '50', 'N/A']
Row 8: Bad row: ['GE', '', '37.23']
Row 13: Bad row: ['INTC', '', '21.84']
Row 17: Bad row: ['MCD', '', '51.11']
Row 19: Bad row: ['MO', '', '70.09']
Row 22: Bad row: ['PFE', '', '26.40']
Row 26: Bad row: ['VZ', '', '42.92']
Number of valid rows processed: 20
```

また、有効なデータでプログラムが正しく動作することも確認しましょう。Python インタープリタで次のコードを実行します。

```python
valid_port = read_csv_as_dicts('valid.csv', types=[str, int, float])
print(f"Number of valid rows processed: {len(valid_port)}")
```

すべての行がエラーなく処理されることが確認できるはずです。以下は、出力の例です。

```
Number of valid rows processed: 17
```

Python インタープリタを終了するには、次のコマンドを実行します。

```python
exit()
```

これで、コードはより堅牢になりました。不適切な行をスキップすることで、無効なデータを適切に処理できるようになり、クラッシュすることがなくなります。これにより、プログラムはより信頼性が高く、使いやすくなります。
