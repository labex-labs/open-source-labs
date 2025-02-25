# リストにすべての値が含まれているかどうかを確認する

`includes_all(lst, values)` という名前の関数を書きます。この関数は 2 つのリストをパラメータとして受け取ります。この関数は、`values` リストのすべての値が `lst` リストに含まれているかどうかを確認する必要があります。すべての値が含まれている場合、関数は `True` を返す必要があります。どれか 1 つの値が含まれていない場合、関数は `False` を返す必要があります。

この問題を解決するには、次のことを行う必要があります。

1. `for` ループを使用して、`values` リストの各値を反復処理します。
2. `in` 演算子を使用して、現在の値が `lst` リストに含まれているかどうかを確認します。
3. 値が含まれていない場合、`False` を返します。
4. すべての値が含まれている場合、`True` を返します。

```python
def includes_all(lst, values):
  for v in values:
    if v not in lst:
      return False
  return True
```

```python
includes_all([1, 2, 3, 4], [1, 4]) # True
includes_all([1, 2, 3, 4], [1, 5]) # False
```
