# 関数に基づくリストの共通部分

`intersection_by(a, b, fn)` という関数を書きます。この関数は、2 つのリスト `a` と `b` と、関数 `fn` を受け取ります。この関数は、両方のリストの各要素に提供された関数を適用した後、両方のリストに存在する要素のリストを返す必要があります。

### 入力

- 2 つのリスト `a` と `b` (1 <= len(a), len(b) <= 1000)
- 1 つの引数を受け取り、値を返す関数 `fn`

### 出力

- 両方のリストの各要素に提供された関数を適用した後、両方のリストに存在する要素のリスト。

```python
def intersection_by(a, b, fn):
  _b = set(map(fn, b))
  return [item for item in a if fn(item) in _b]
```

```python
from math import floor

intersection_by([2.1, 1.2], [2.3, 3.4], floor) # [2.1]
```
