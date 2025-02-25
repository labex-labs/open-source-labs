# 出現回数を数える

`count_occurrences(lst, val)` という関数を書きましょう。この関数は、リスト `lst` と値 `val` を引数として受け取り、`lst` の中で `val` が何回出現するかを返します。関数は、出現回数を数えるために組み込みの `list.count()` メソッドを使用する必要があります。

```python
def count_occurrences(lst, val):
  return lst.count(val)
```

```python
count_occurrences([1, 1, 2, 1, 2, 3], 1) # 3
```
