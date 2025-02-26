# 例外の発生

`cofollow.py` ファイルでは、コルーチン `printer()` を作成しました。このコードを変更して、次のように例外をキャッチして報告するようにします。

```python
# cofollow.py
...
@consumer
def printer():
    while True:
        try:
            item = yield
            print(item)
        except Exception as e:
            print('ERROR: %r' % e)
```

次に、実験を試してみましょう。

```python
>>> from cofollow import printer
>>> p = printer()
>>> p.send('hello')
hello
>>> p.send(42)
42
>>> p.throw(ValueError('It failed'))
ERROR: ValueError('It failed',)
>>> try:
        int('n/a')
    except ValueError as e:
        p.throw(e)

ERROR: ValueError("invalid literal for int() with base 10: 'n/a'",)
>>>
```

実行中のジェネレータが例外によって終了しないことに注意してください。これは、`yield` ステートメントが値を受け取る代わりにエラーを通知するだけのものです。
