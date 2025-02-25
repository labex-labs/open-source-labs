# リスト内の重複を確認する

`has_duplicates(lst)` という名前の Python 関数を作成します。この関数は、引数としてリストを受け取り、リストに重複する値が含まれている場合は `True` を返し、そうでない場合は `False` を返します。

この問題を解くには、次の手順を使用できます。

1. `set()` 関数を使用して、リストから重複する値を削除します。
2. 元のリストの長さとセットの長さを比較します。もし同じであれば、重複する値はありません。もし異なっていれば、重複する値があります。

```python
def has_duplicates(lst):
  return len(lst)!= len(set(lst))
```

```python
x = [1, 2, 3, 4, 5, 5]
y = [1, 2, 3, 4, 5]
has_duplicates(x) # True
has_duplicates(y) # False
```
