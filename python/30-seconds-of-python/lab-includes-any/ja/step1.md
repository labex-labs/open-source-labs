# リストの値が別のリストに含まれているかどうかを確認する

2 つのリストを引数として受け取る関数`includes_any(lst, values)`を書きます。この関数は、`values`の要素が`lst`に含まれているかどうかを確認する必要があります。1 つでも値が見つかった場合、関数は`True`を返し、そうでなければ`False`を返す必要があります。

この問題を解くには、`for`ループを使って`values`の各値を反復処理できます。その後、`in`演算子を使って値が`lst`に含まれているかどうかを確認できます。値が見つかった場合は`True`を返します。値が見つからなかった場合は`False`を返します。

```python
def includes_any(lst, values):
  for v in values:
    if v in lst:
      return True
  return False
```

```python
includes_any([1, 2, 3, 4], [2, 9]) # True
includes_any([1, 2, 3, 4], [8, 9]) # False
```
