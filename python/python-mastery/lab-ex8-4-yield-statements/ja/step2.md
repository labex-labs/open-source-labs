# ジェネレータでの例外処理

このステップでは、ジェネレータとコルーチンで例外を処理する方法を学びます。まずは、例外とは何かを理解しましょう。例外とは、プログラムの実行中に発生し、プログラムの命令の通常の流れを中断するイベントです。Python では、`throw()` メソッドを使用して、ジェネレータとコルーチンで例外を処理することができます。

## コルーチンの理解

コルーチンは、特殊な種類のジェネレータです。主に値を生成する通常のジェネレータとは異なり、コルーチンは値を消費することも（`send()` メソッドを使用）、値を生成することもできます。`cofollow.py` ファイルには、コルーチンの簡単な実装があります。

WebIDE エディタで `cofollow.py` ファイルを開きましょう。中身のコードは次の通りです。

```python
def consumer(func):
    def start(*args,**kwargs):
        c = func(*args,**kwargs)
        next(c)
        return c
    return start

@consumer
def printer():
    while True:
        item = yield
        print(item)
```

では、このコードを分解してみましょう。`consumer` はデコレータです。デコレータは、別の関数を引数として受け取り、それにいくつかの機能を追加してから、修正された関数を返す関数です。この場合、`consumer` デコレータは自動的にジェネレータを最初の `yield` 文まで進めます。これは、ジェネレータが値を受け取る準備をするために重要です。

`printer()` コルーチンは、`@consumer` デコレータで定義されています。`printer()` 関数の中には、無限の `while` ループがあります。`item = yield` 文がポイントです。これはコルーチンの実行を一時停止し、値を受け取るのを待ちます。コルーチンに値が送られると、実行が再開され、受け取った値が出力されます。

## コルーチンに例外処理を追加する

では、`printer()` コルーチンを修正して例外を処理するようにしましょう。`cofollow.py` の `printer()` 関数を次のように更新します。

```python
@consumer
def printer():
    while True:
        try:
            item = yield
            print(item)
        except Exception as e:
            print('ERROR: %r' % e)
```

`try` ブロックには、例外を引き起こす可能性のあるコードが含まれています。この場合、値を受け取って出力するコードです。`try` ブロックで例外が発生すると、実行は `except` ブロックにジャンプします。`except` ブロックは例外をキャッチし、エラーメッセージを出力します。これらの変更を加えた後、ファイルを保存します。

## コルーチンでの例外処理の実験

では、コルーチンに例外を投げる実験を始めましょう。ターミナルを開き、次のコマンドを使用して Python インタープリタを起動します。

```bash
cd ~/project
python3
```

### 実験 1: 基本的なコルーチンの使用

```python
>>> from cofollow import printer
>>> p = printer()
>>> p.send('hello')  # Send a value to the coroutine
hello
>>> p.send(42)  # Send another value
42
```

ここでは、まず `cofollow` モジュールから `printer` コルーチンをインポートします。次に、`printer` コルーチンのインスタンス `p` を作成します。`send()` メソッドを使用して、コルーチンに値を送ります。見ての通り、コルーチンは送られた値を問題なく処理します。

### 実験 2: コルーチンに例外を投げる

```python
>>> p.throw(ValueError('It failed'))  # Throw an exception into the coroutine
ERROR: ValueError('It failed')
```

この実験では、`throw()` メソッドを使用して、`ValueError` 例外をコルーチンに注入します。`printer()` コルーチンの `try-except` ブロックが例外をキャッチし、エラーメッセージを出力します。これは、例外処理が期待通りに機能していることを示しています。

### 実験 3: コルーチンに実際の例外を投げる

```python
>>> try:
...     int('n/a')  # This will raise a ValueError
... except ValueError as e:
...     p.throw(e)  # Throw the caught exception into the coroutine
...
ERROR: ValueError("invalid literal for int() with base 10: 'n/a'")
```

ここでは、まず文字列 `'n/a'` を整数に変換しようとしますが、これは `ValueError` を引き起こします。この例外をキャッチしてから、`throw()` メソッドを使用してコルーチンに渡します。コルーチンは例外をキャッチし、エラーメッセージを出力します。

### 実験 4: コルーチンが引き続き実行されることを確認する

```python
>>> p.send('still working')  # The coroutine continues to run after handling exceptions
still working
```

例外を処理した後、`send()` メソッドを使用してコルーチンに別の値を送ります。コルーチンはまだアクティブで、新しい値を処理することができます。これは、コルーチンがエラーに遭遇した後も引き続き実行できることを示しています。

## 要点

1. ジェネレータとコルーチンは、`yield` 文の位置で例外を処理することができます。これは、コルーチンが値を待っているときや処理しているときに発生するエラーをキャッチして処理できることを意味します。
2. `throw()` メソッドを使用すると、ジェネレータまたはコルーチンに例外を注入することができます。これは、テストやコルーチンの外で発生したエラーを処理するのに役立ちます。
3. ジェネレータで適切に例外を処理することで、エラーが発生しても引き続き実行できる堅牢でエラー耐性のあるジェネレータを作成することができます。これにより、コードがより信頼性が高く、保守が容易になります。

Python インタープリタを終了するには、`exit()` と入力するか、`Ctrl+D` を押します。
