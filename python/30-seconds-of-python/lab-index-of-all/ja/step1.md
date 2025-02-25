# 値のすべてのインデックス

`index_of_all(lst, value)` という名前の Python 関数を書きましょう。この関数は、リスト `lst` と値 `value` を引数として受け取り、`lst` 内の `value` のすべての出現箇所のインデックスのリストを返します。

この問題を解くには、`enumerate()` とリスト内包表記を使って、各要素が `value` と等しいかどうかをチェックし、結果に `i` を追加します。

```python
def index_of_all(lst, value):
  return [i for i, x in enumerate(lst) if x == value]
```

```python
index_of_all([1, 2, 1, 4, 5, 1], 1) # [0, 2, 5]
index_of_all([1, 2, 3, 4], 6) # []
```
