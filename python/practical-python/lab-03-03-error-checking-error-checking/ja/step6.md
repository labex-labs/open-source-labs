# 複数のエラーのキャッチ

複数の `except` ブロックを使用して、さまざまな種類の例外をキャッチすることができます。

```python
try:
...
except LookupError as e:
...
except RuntimeError as e:
...
except IOError as e:
...
except KeyboardInterrupt as e:
...
```

あるいは、それらを処理する文が同じ場合、それらをグループ化することができます。

```python
try:
...
except (IOError,LookupError,RuntimeError) as e:
...
```
