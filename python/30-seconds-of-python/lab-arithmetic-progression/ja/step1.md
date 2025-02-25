# 等差数列

`arithmetic_progression(n, lim)` という関数を書きなさい。この関数は、2つの正の整数 `n` と `lim` を引数に取り、`n` から始まり `lim` までの等差数列の数のリストを返します。この関数は、適切な開始値、ステップ値、終了値を使って `range()` と `list()` を使ってリストを生成する必要があります。

### 入力

- 2つの正の整数 `n` と `lim`。ここで、`n` は開始数で、`lim` は制限です。

### 出力

- `n` から始まり `lim` までの等差数列の数のリスト。

```python
def arithmetic_progression(n, lim):
  return list(range(n, lim + 1, n))
```

```python
arithmetic_progression(5, 25) # [5, 10, 15, 20, 25]
```
