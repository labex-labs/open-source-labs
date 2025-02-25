# リスト要素のオフセット

`offset(lst, offset)` という関数を書きます。この関数は、リスト `lst` と整数 `offset` を引数として受け取り、指定された数の要素をリストの末尾に移動した新しいリストを返します。`offset` が正の場合、最初の `offset` 要素をリストの末尾に移動します。`offset` が負の場合、最後の `offset` 要素をリストの先頭に移動します。

```python
def offset(lst, offset):
  return lst[offset:] + lst[:offset]
```

```python
offset([1, 2, 3, 4, 5], 2) # [3, 4, 5, 1, 2]
offset([1, 2, 3, 4, 5], -2) # [4, 5, 1, 2, 3]
```
