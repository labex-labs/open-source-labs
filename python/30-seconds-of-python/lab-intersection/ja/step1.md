# リストの積集合

2 つのリスト `a` と `b` を入力として受け取り、`a` と `b` の両方に存在する要素のみを含む新しいリストを返す関数 `list_intersection(a, b)` を書きます。共通要素がない場合は、関数は空のリストを返す必要があります。

```python
def intersection(a, b):
  _a, _b = set(a), set(b)
  return list(_a & _b)
```

```python
intersection([1, 2, 3], [4, 3, 2]) # [2, 3]
```
