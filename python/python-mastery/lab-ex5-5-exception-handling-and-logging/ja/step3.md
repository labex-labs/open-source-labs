# ロギングの実装

このステップでは、コードを改善します。単純な print メッセージを使用する代わりに、Python の `logging` モジュールを使用して適切なロギングを行います。ロギングは、プログラムが何をしているかを追跡する素晴らしい方法です。特に、エラーの処理やコードの流れを理解する際に役立ちます。

## ロギングモジュールの理解

Python の `logging` モジュールは、アプリケーションからログメッセージを送信する柔軟な方法を提供します。単純な print 文を使用するよりもはるかに強力です。以下はその機能です。

1. 異なるログレベル (DEBUG、INFO、WARNING、ERROR、CRITICAL): これらのレベルは、メッセージの重要度を分類するのに役立ちます。たとえば、DEBUG は開発中に役立つ詳細情報用で、CRITICAL はプログラムを停止させる可能性のある深刻なエラー用です。
2. 設定可能な出力形式：ログメッセージの外見を決定できます。たとえば、タイムスタンプやその他の有用な情報を追加することができます。
3. メッセージを異なる出力先 (コンソール、ファイルなど) に送信できる：ログメッセージをコンソールに表示したり、ファイルに保存したり、リモートサーバーに送信したりすることができます。
4. 重大度に基づくログフィルタリング：ログレベルに基づいて表示するメッセージを制御できます。

## reader.py にロギングを追加する

では、コードを変更してロギングモジュールを使用しましょう。`reader.py` ファイルを開きます。

まず、`logging` モジュールをインポートし、このモジュール用のロガーを設定する必要があります。ファイルの先頭に次のコードを追加します。

```python
import logging

# Set up a logger for this module
logger = logging.getLogger(__name__)
```

`import logging` 文は `logging` モジュールをインポートし、その関数を使用できるようにします。`logging.getLogger(__name__)` は、この特定のモジュール用のロガーを作成します。`__name__` を使用することで、ロガーがモジュールに関連する一意の名前を持つことが保証されます。

次に、`convert_csv()` 関数を変更して、print 文の代わりにロギングを使用します。以下は更新されたコードです。

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
            # Log a warning message for bad rows
            logger.warning(f"Row {row_idx}: Bad row: {row}")
            # Log the reason at debug level
            logger.debug(f"Row {row_idx}: Reason: {str(e)}")
            continue

    return result
```

主な変更点は以下の通りです。

- エラーメッセージの `print()` を `logger.warning()` に置き換えました。これにより、メッセージは適切な警告レベルでログに記録され、後でその可視性を制御できます。
- 例外の詳細を含む新しい `logger.debug()` メッセージを追加しました。これにより、何がうまくいかなかったかに関するより多くの情報が得られますが、ログレベルが DEBUG またはそれ以下に設定されている場合にのみ表示されます。
- `str(e)` は例外を文字列に変換するため、ログメッセージにエラーの理由を表示できます。

これらの変更を加えた後、ファイルを保存します。

## ロギングのテスト

ロギングを有効にしてコードをテストしましょう。ターミナルで次のコマンドを実行して Python インタープリタを開きます。

```bash
python3
```

Python インタープリタに入ったら、次のコードを実行します。

```python
import logging
import reader

# Configure logging level to see all messages
logging.basicConfig(level=logging.DEBUG)

port = reader.read_csv_as_dicts('missing.csv', types=[str, int, float])
print(f"Number of valid rows processed: {len(port)}")
```

ここでは、まず `logging` モジュールと `reader` モジュールをインポートします。次に、`logging.basicConfig(level=logging.DEBUG)` を使用してログレベルを DEBUG に設定します。これは、DEBUG、INFO、WARNING、ERROR、CRITICAL を含むすべてのログメッセージが表示されることを意味します。その後、`reader` モジュールの `read_csv_as_dicts` 関数を呼び出し、処理された有効な行の数を表示します。

次のような出力が表示されるはずです。

```
WARNING:reader:Row 4: Bad row: ['C', '', '53.08']
DEBUG:reader:Row 4: Reason: invalid literal for int() with base 10: ''
WARNING:reader:Row 7: Bad row: ['DIS', '50', 'N/A']
DEBUG:reader:Row 7: Reason: could not convert string to float: 'N/A'
...
Number of valid rows processed: 20
```

ロギングモジュールが各メッセージにプレフィックスを追加し、ログレベル (WARNING/DEBUG) とモジュール名が表示されることに注意してください。

では、ログレベルを変更して警告のみを表示する場合を見てみましょう。Python インタープリタで次のコードを実行します。

```python
# Reset the logging configuration
import logging
logging.basicConfig(level=logging.WARNING)

port = reader.read_csv_as_dicts('missing.csv', types=[str, int, float])
```

今回は、`logging.basicConfig(level=logging.WARNING)` を使用してログレベルを WARNING に設定します。これで、WARNING メッセージのみが表示され、DEBUG メッセージは非表示になります。

```
WARNING:reader:Row 4: Bad row: ['C', '', '53.08']
WARNING:reader:Row 7: Bad row: ['DIS', '50', 'N/A']
...
```

これは、異なるログレベルを使用する利点を示しています。コードを変更することなく、ログに表示される詳細度を制御できます。

Python インタープリタを終了するには、次のコマンドを実行します。

```python
exit()
```

おめでとうございます！Python プログラムに適切な例外処理とロギングを実装しました。これにより、コードがより信頼性が高くなり、エラーが発生したときにより良い情報が得られます。
