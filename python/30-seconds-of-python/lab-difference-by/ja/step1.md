# 関数に基づくリストの差分

`difference_by(a, b, fn)` という名前の関数を作成します。この関数には3つのパラメータが渡されます。

- `a`: 要素のリスト
- `b`: 要素のリスト
- `fn`: 両方のリストの各要素に適用される関数

この関数は、両方のリストの各要素に提供された関数 `fn` を適用した後、リスト `a` には含まれているがリスト `b` には含まれていない要素のリストを返す必要があります。

この問題を解くには、次の手順を辿ることができます。

1. `map()` を使って `fn` を `b` の各要素に適用し、`set` を作成します。
2. `a` の `fn` と組み合わせてリスト内包表記を使って、以前作成した `_b` に含まれていない値のみを残します。

```python
def difference_by(a, b, fn):
  _b = set(map(fn, b))
  return [item for item in a if fn(item) not in _b]
```

```python
from math import floor

difference_by([2.1, 1.2], [2.3, 3.4], floor) # [1.2]
difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x'])
# [ { x: 2 } ]
```
