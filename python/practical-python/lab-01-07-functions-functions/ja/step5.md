# 例外の発生

例外を発生させるには、`raise` 文を使用します。

```python
raise RuntimeError('What a kerfuffle')
```

これにより、例外のトレースバック付きでプログラムが中止されます。`try-except` ブロックによってキャッチされない限りです。

```bash
% python3 foo.py
Traceback (most recent call last):
  File "foo.py", line 21, in <module>
    raise RuntimeError("What a kerfuffle")
RuntimeError: What a kerfuffle
```
