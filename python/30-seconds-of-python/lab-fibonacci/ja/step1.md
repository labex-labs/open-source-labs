# フィボナッチ

整数 `n` をパラメータとして受け取り、n 番目の項までのフィボナッチ数列を含むリストを返す `fibonacci(n)` という関数を書きます。

この問題を解くには、次の手順に従うことができます。

1. `sequence` という空のリストを作成します。
2. `n` が 0 以下の場合、`sequence` リストに 0 を追加してリストを返します。
3. `sequence` リストに 0 と 1 を追加します。
4. while ループを使って、`sequence` リストの最後の 2 つの数の和をリストの末尾に追加し、リストの長さが `n` に達するまで続けます。
5. `sequence` リストを返します。

```python
def fibonacci(n):
  if n <= 0:
    return [0]
  sequence = [0, 1]
  while len(sequence) <= n:
    next_value = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
    sequence.append(next_value)
  return sequence
```

```python
fibonacci(7) # [0, 1, 1, 2, 3, 5, 8, 13]
```
