# リストを N チャンクに分割する

`chunk_into_n(lst, n)` という Python 関数を書きましょう。この関数は、リスト `lst` と整数 `n` を入力として受け取り、`n` 個の小さなリストのリストを返します。各小さなリストは、元のリストから等しい数の要素を含んでいます。元のリストを `n` 個の小さなリストに均等に分割できない場合、最後のチャンクは残りの要素を含みます。

この問題を解くには、次の手順に従うことができます。

1. 元のリストの長さを `n` で割り、`math.ceil()` 関数を使って最も近い整数に切り上げることで、各チャンクのサイズを計算します。
2. `list()` と `range()` 関数を使って、サイズ `n` の新しいリストを作成します。
3. `map()` 関数を使って、新しいリストの各要素を、サイズ `size` の元のリストのチャンクにマッピングします。
4. 小さなリストのリストを返します。

あなたの関数は次のシグネチャを持つ必要があります。

```python
def chunk_into_n(lst: list, n: int) -> list:
```

```python
from math import ceil

def chunk_into_n(lst, n):
  size = ceil(len(lst) / n)
  return list(
    map(lambda x: lst[x * size:x * size + size],
    list(range(n)))
  )
```

```python
chunk_into_n([1, 2, 3, 4, 5, 6, 7], 4) # [[1, 2], [3, 4], [5, 6], [7]]
```
