# 範囲でリストを初期化する

`initialize_list_with_range(end, start=0, step=1)`という関数を書きます。この関数は、指定された範囲の数値を含むリストを初期化します。ここで、`start`と`end`はその範囲に含まれ、共通の差分は`step`です。

この関数は、適切な長さのリストを返し、与えられた範囲内の望ましい値で埋められています。

### 入力

- `end`（整数） - 範囲の終端（含まれます）。
- `start`（整数、オプション） - 範囲の始端（含まれます）。デフォルトは 0。
- `step`（整数、オプション） - 範囲内の各数値間の共通の差分。デフォルトは 1。

### 出力

- 指定された範囲の数値を含むリスト。

```python
def initialize_list_with_range(end, start = 0, step = 1):
  return list(range(start, end + 1, step))
```

```python
initialize_list_with_range(5) # [0, 1, 2, 3, 4, 5]
initialize_list_with_range(7, 3) # [3, 4, 5, 6, 7]
initialize_list_with_range(9, 0, 2) # [0, 2, 4, 6, 8]
```
