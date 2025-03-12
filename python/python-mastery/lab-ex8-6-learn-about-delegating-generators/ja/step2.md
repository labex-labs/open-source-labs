# コルーチンでの `yield from` の使用

このステップでは、より実用的なアプリケーションのために、コルーチンと共に `yield from` 文をどのように使用するかを探ります。コルーチンは Python の強力な概念であり、これと `yield from` を組み合わせる方法を理解することで、コードを大幅に簡素化できます。

## コルーチンとメッセージの受け渡し

コルーチンは、`yield` 文を通じて値を受け取ることができる特殊な関数です。データ処理やイベントハンドリングなどのタスクに非常に役立ちます。`cofollow.py` ファイルには `consumer` デコレータがあります。このデコレータは、コルーチンを最初の `yield` ポイントまで自動的に進めることで、コルーチンのセットアップを支援します。つまり、手動でコルーチンを開始する必要はなく、デコレータがその処理を行ってくれます。

値を受け取り、その型を検証するコルーチンを作成しましょう。以下のように行うことができます。

1. まず、エディタで `cofollow.py` ファイルを開きます。ターミナルで次のコマンドを使用して、正しいディレクトリに移動できます。

```bash
cd /home/labex/project
```

2. 次に、`cofollow.py` ファイルの末尾に次の `receive` 関数を追加します。この関数は、メッセージを受け取り、その型を検証するコルーチンです。

```python
def receive(expected_type):
    """
    A coroutine that receives a message and validates its type.
    Returns the received message if it matches the expected type.
    """
    msg = yield
    assert isinstance(msg, expected_type), f'Expected type {expected_type}'
    return msg
```

この関数の動作は以下の通りです。

- 式を伴わない `yield` を使用して値を受け取ります。コルーチンに値が送信されると、この `yield` 文がそれを捕捉します。
- `isinstance` 関数を使用して、受け取った値が期待される型であるかどうかを確認します。型が一致しない場合、`AssertionError` を発生させます。
- 型チェックが通過すると、値を返します。

3. これで、`receive` 関数と共に `yield from` を使用するコルーチンを作成しましょう。この新しいコルーチンは、整数のみを受け取り、表示します。

```python
@consumer
def print_ints():
    """
    A coroutine that receives and prints integers only.
    Uses yield from to delegate to the receive coroutine.
    """
    while True:
        val = yield from receive(int)
        print('Got:', val)
```

4. このコルーチンをテストするには、Python シェルを開き、次のコードを実行します。

```python
from cofollow import print_ints

p = print_ints()
p.send(42)
p.send(13)
try:
    p.send('13')  # This should raise an AssertionError
except AssertionError as e:
    print(f"Error: {e}")
```

以下の出力が表示されるはずです。

```
Got: 42
Got: 13
Error: Expected type <class 'int'>
```

## コルーチンでの `yield from` の動作の理解

`print_ints` コルーチンで `yield from receive(int)` を使用すると、以下の手順が実行されます。

1. 制御が `receive` コルーチンに委任されます。これは、`print_ints` コルーチンが一時停止し、`receive` コルーチンが実行を開始することを意味します。
2. `receive` コルーチンは `yield` を使用して値を受け取ります。送信される値を待機します。
3. `print_ints` に値が送信されると、実際には `receive` がそれを受け取ります。`yield from` 文が `print_ints` から `receive` への値の受け渡しを処理します。
4. `receive` コルーチンは、受け取った値の型を検証します。型が正しい場合、値を返します。
5. 返された値は、`print_ints` コルーチン内の `yield from` 式の結果となります。つまり、`print_ints` 内の `val` 変数には、`receive` が返した値が割り当てられます。

`yield from` を使用すると、直接 `yield` と受け取りを処理する場合よりもコードが読みやすくなります。コルーチン間の値の受け渡しの複雑さを抽象化します。

## より高度な型チェックコルーチンの作成

より複雑な型検証を処理するために、ユーティリティ関数を拡張しましょう。以下のように行うことができます。

1. `cofollow.py` ファイルに次の関数を追加します。

```python
def receive_dict():
    """Receive and validate a dictionary"""
    result = yield from receive(dict)
    return result

def receive_str():
    """Receive and validate a string"""
    result = yield from receive(str)
    return result

@consumer
def process_data():
    """Process different types of data using the receive utilities"""
    while True:
        print("Waiting for a string...")
        name = yield from receive_str()
        print(f"Got string: {name}")

        print("Waiting for a dictionary...")
        data = yield from receive_dict()
        print(f"Got dictionary with {len(data)} items: {data}")

        print("Processing complete for this round.")
```

2. 新しいコルーチンをテストするには、Python シェルを開き、次のコードを実行します。

```python
from cofollow import process_data

proc = process_data()
proc.send("John Doe")
proc.send({"age": 30, "city": "New York"})
proc.send("Jane Smith")
try:
    proc.send(123)  # This should raise an AssertionError
except AssertionError as e:
    print(f"Error: {e}")
```

以下のような出力が表示されるはずです。

```
Waiting for a string...
Got string: John Doe
Waiting for a dictionary...
Got dictionary with 2 items: {'age': 30, 'city': 'New York'}
Processing complete for this round.
Waiting for a string...
Got string: Jane Smith
Waiting for a dictionary...
Error: Expected type <class 'dict'>
```

`yield from` 文により、コードがよりクリーンで読みやすくなります。コルーチン間のメッセージの受け渡しの詳細に取り組むのではなく、プログラムの高レベルなロジックに集中することができます。
