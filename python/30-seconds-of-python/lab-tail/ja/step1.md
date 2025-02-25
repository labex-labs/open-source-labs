# リストの末尾の要素

引数としてリストを受け取り、最初の要素を除いたリストのすべての要素を返す関数 `tail(lst)` を作成します。リストに要素が 1 つだけ含まれている場合は、そのままのリストを返します。

```python
def tail(lst):
  return lst[1:] if len(lst) > 1 else lst
```

```python
tail([1, 2, 3]) # [2, 3]
tail([1]) # [1]
```
