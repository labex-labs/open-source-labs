# リストをチャンクに分割する

`chunk(lst, size)` という関数を書きましょう。この関数は、リスト `lst` と正の整数 `size` を引数として受け取り、最大サイズが `size` の小さなリストのリストを返します。`lst` の長さが `size` で割り切れない場合、返されるリストの最後のリストは残りの要素を含む必要があります。

```python
from math import ceil

def chunk(lst, size):
  return list(
    map(lambda x: lst[x * size:x * size + size],
      list(range(ceil(len(lst) / size)))))
```

```python
chunk([1, 2, 3, 4, 5], 2) # [[1, 2], [3, 4], [5]]
```
