# 最小値のキー

## 問題

辞書 `d` を引数として受け取り、辞書内の最小値のキーを返す関数 `key_of_min(d)` を書きなさい。

この問題を解くには、`key` パラメータを `dict.get()` に設定した組み込みの `min()` 関数を使用できます。これにより、辞書内の最小値のキーが返されます。

## 例

```python
key_of_min({'a':4, 'b':0, 'c':13}) # 'b'
```

この例では、辞書 `{'a':4, 'b':0, 'c':13}` が `key_of_min()` 関数に引数として渡されます。関数は、辞書内の最小値に対応するキー `'b'` を返します。
