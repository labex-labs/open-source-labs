# 数値を桁ごとに分割する

非負整数 `n` を入力として受け取り、その桁のリストを返す関数 `digitize(n)` を書いてください。この関数は、以下の手順を実行することでこれを達成する必要があります。

1. 入力された数値 `n` を文字列に変換します。
2. `map()` 関数と `int` 関数を組み合わせて、文字列内の各文字を整数に変換します。
3. 結果として得られる整数のリストを返します。

たとえば、入力された数値が `123` の場合、関数はリスト `[1, 2, 3]` を返す必要があります。

```python
def digitize(n):
  return list(map(int, str(n)))
```

```python
digitize(123) # [1, 2, 3]
```
