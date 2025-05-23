# 範囲内の数

`in_range(n, start, end = 0)` という関数を作成します。この関数には以下の 3 つのパラメータが渡されます。

- `n`：範囲内にあるかどうかを確認する数
- `start`：範囲の始点
- `end`：範囲の終点（省略可能。デフォルト値は 0）

与えられた数 `n` が指定された範囲内にある場合、関数は `True` を返します。それ以外の場合は `False` を返します。`end` パラメータが指定されない場合、範囲は `0` から `start` までと見なされます。

```python
def in_range(n, start, end = 0):
  return start <= n <= end if end >= start else end <= n <= start
```

```python
in_range(3, 2, 5) # True
in_range(3, 4) # True
in_range(2, 3, 5) # False
in_range(3, 2) # False
```
