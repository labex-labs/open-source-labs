# 真の場合に関数を適用する

`when` という名前の関数を書きます。この関数は 2 つの引数を取ります。述語関数 `predicate` と、`when_true` として適用する関数です。`when` 関数は、単一の引数 `x` を取る新しい関数を返す必要があります。新しい関数は、`predicate(x)` の値が `True` であるかどうかを確認する必要があります。もしそうなら、新しい関数は `when_true(x)` を呼び出し、結果を返す必要があります。そうでなければ、新しい関数は `x` を返す必要があります。

```python
def when(predicate, when_true):
  return lambda x: when_true(x) if predicate(x) else x
```

```python
double_even_numbers = when(lambda x: x % 2 == 0, lambda x : x * 2)
double_even_numbers(2) # 4
double_even_numbers(1) # 1
```
