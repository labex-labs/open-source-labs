# 最小値のキー

`key_of_min(d)` という関数を書きましょう。この関数は辞書 `d` を引数に取り、辞書内の最小値のキーを返します。

この問題を解くには、組み込みの `min()` 関数を使用して、`key` パラメータを `dict.get()` に設定します。これにより、辞書内の最小値のキーが返されます。

```python
def key_of_min(d):
  return min(d, key = d.get)
```

```python
key_of_min({'a':4, 'b':0, 'c':13}) # b
```
