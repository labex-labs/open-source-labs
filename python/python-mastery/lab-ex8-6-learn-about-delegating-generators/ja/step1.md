# 例: メッセージの受信

演習8.3では、コルーチンの定義を見ました。コルーチンは、データを送信する関数でした。たとえば：

```python
>>> from cofollow import consumer
>>> @consumer
    def printer():
        while True:
            item = yield
            print('Got:', item)

>>> p = printer()
>>> p.send('Hello')
Got: Hello
>>> p.send('World')
Got: World
>>>
```

当時、値を受け取るために `yield` を使用することが面白かったかもしれません。しかし、本当にコードを見ると、とても奇妙に見えます - そんな裸の `yield` は何をしているのでしょう？

`cofollow.py` ファイルに、次の関数を定義します：

```python
def receive(expected_type):
    msg = yield
    assert isinstance(msg, expected_type), 'Expected type %s' % (expected_type)
    return msg
```

この関数はメッセージを受け取りますが、その後、期待される型であることを検証します。試してみましょう：

```python
>>> from cofollow import consumer, receive
>>> @consumer
    def print_ints():
        while True:
             val = yield from receive(int)
             print('Got:', val)

>>> p = print_ints()
>>> p.send(42)
Got: 42
>>> p.send(13)
Got: 13
>>> p.send('13')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
...
AssertionError: Expected type <class 'int'>
>>>
```

読みやすさの点から見ると、`yield from receive(int)` ステートメントはもう少し分かりやすいです - この関数は、特定の型のメッセージを受け取るまで待機することを示しています。

次に、`coticker.py` 内のすべてのコルーチンを変更して、新しい `receive()` 関数を使用し、演習8.3のコードがまだ機能することを確認します。
