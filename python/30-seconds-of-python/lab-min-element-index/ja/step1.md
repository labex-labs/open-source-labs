# 最小要素のインデックス

整数のリスト `arr` を引数として受け取り、リスト内の最小値を持つ要素のインデックスを返す関数 `min_element_index(arr)` を作成します。

この問題を解くには、`min()` 関数を使ってリスト内の最小値を取得し、その後 `list.index()` メソッドを使ってそのインデックスを返します。

```python
def min_element_index(arr):
  return arr.index(min(arr))
```

```python
min_element_index([3, 5, 2, 6, 10, 7, 9]) # 2
```
