# 最後の一致するインデックスを見つける

引数としてリスト `lst` と関数 `fn` を受け取る関数 `find_last_index(lst, fn)` を書きます。この関数は、`fn` が `True` を返す `lst` の最後の要素のインデックスを返す必要があります。どの要素も条件を満たさない場合、関数は `-1` を返す必要があります。

```python
def find_last_index(lst, fn):
  return len(lst) - 1 - next(i for i, x in enumerate(lst[::-1]) if fn(x))
```

```python
find_last_index([1, 2, 3, 4], lambda n: n % 2 == 1) # 2
```
