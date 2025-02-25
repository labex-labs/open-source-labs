# 等比数列

`geometric_progression` という名前の関数を書きましょう。この関数は 3 つのパラメータを受け取ります。

- `end`：範囲の終端を表す整数（含まれます）
- `start`：範囲の始端を表すオプショナルな整数（含まれます）。デフォルト値は `1`
- `step`：2 つの項の間の公比を表すオプショナルな整数。デフォルト値は `2`

関数は、2 つの項の間の比が `step` である指定された範囲の数を含むリストを返す必要があります。リストは `start` から始まり、`end` で終わるものとします。

`step` が `1` に等しい場合、関数はエラーを返す必要があります。

適切な長さのリストを作成するために、`range()`、`math.log()`、`math.floor()` とリスト内包表記を使用し、各要素に対してステップを適用する必要があります。

```python
from math import floor, log

def geometric_progression(end, start=1, step=2):
  return [start * step ** i for i in range(floor(log(end / start)
          / log(step)) + 1)]
```

```python
geometric_progression(256) # [1, 2, 4, 8, 16, 32, 64, 128, 256]
geometric_progression(256, 3) # [3, 6, 12, 24, 48, 96, 192]
geometric_progression(256, 1, 4) # [1, 4, 16, 64, 256]
```
