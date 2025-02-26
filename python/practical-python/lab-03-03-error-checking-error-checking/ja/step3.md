# 例外処理

例外は最初の一致する `except` に伝播します。

```python
def grok():
  ...
    raise RuntimeError('Whoa!')   # ここで例外が発生します

def spam():
    grok()                        # 例外を発生させる呼び出し

def bar():
    try:
       spam()
    except RuntimeError as e:     # ここで例外がキャッチされます
      ...

def foo():
    try:
         bar()
    except RuntimeError as e:     # 例外はここには到達しません
      ...

foo()
```

例外を処理するには、`except` ブロックに文を記述します。エラーを処理するために必要な任意の文を追加できます。

```python
def grok():...
    raise RuntimeError('Whoa!')

def bar():
    try:
      grok()
    except RuntimeError as e:   # ここで例外がキャッチされます
        statements              # この文を使用します
        statements
      ...

bar()
```

処理後、実行は `try-except` の直後の最初の文から再開されます。

```python
def grok():...
    raise RuntimeError('Whoa!')

def bar():
    try:
      grok()
    except RuntimeError as e:   # ここで例外がキャッチされます
        statements
        statements
      ...
    statements                  # ここで実行が再開されます
    statements                  # そしてここから続行されます
  ...

bar()
```
