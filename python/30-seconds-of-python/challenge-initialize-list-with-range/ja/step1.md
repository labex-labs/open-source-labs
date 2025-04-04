# 範囲でリストを初期化する

## 問題

`initialize_list_with_range(end, start=0, step=1)` という関数を書きなさい。この関数は、指定された範囲の数値を含むリストを初期化します。ここで、`start` と `end` はそれぞれ範囲の始点と終点で、それらは共通の差分 `step` を持ちます。

この関数は、適切な長さのリストを返し、与えられた範囲内の望ましい値で埋められている必要があります。

### 入力

- `end` (整数) - 範囲の終点（含む）。
- `start` (整数、オプション) - 範囲の始点（含む）。デフォルトは 0。
- `step` (整数、オプション) - 範囲内の各数値間の共通の差分。デフォルトは 1。

### 出力

- 指定された範囲の数値を含むリスト。

## 例

```python
initialize_list_with_range(5) # [0, 1, 2, 3, 4, 5]
initialize_list_with_range(7, 3) # [3, 4, 5, 6, 7]
initialize_list_with_range(9, 0, 2) # [0, 2, 4, 6, 8]
```
