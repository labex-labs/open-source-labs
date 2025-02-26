# 例外

例外はエラーを通知するために使用されます。自分で例外を発生させるには、`raise` 文を使用します。

```python
if name not in authorized:
    raise RuntimeError(f'{name} not authorized')
```

例外をキャッチするには、`try-except` を使用します。

```python
try:
    authenticate(username)
except RuntimeError as e:
    print(e)
```
