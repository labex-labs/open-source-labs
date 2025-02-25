# 真の場合に関数を適用する

## 問題

`when` という名前の関数を書きましょう。この関数は 2 つの引数を取ります。述語関数 `predicate` と、`when_true` として適用する関数です。`when` 関数は、単一の引数 `x` を取る新しい関数を返す必要があります。新しい関数は、`predicate(x)` の値が `True` であるかどうかを確認する必要があります。もしそうなら、新しい関数は `when_true(x)` を呼び出し、結果を返す必要があります。そうでなければ、新しい関数は `x` を返す必要があります。

## 例

```python
def double(x):
    return x * 2

def is_even(x):
    return x % 2 == 0

double_even_numbers = when(is_even, double)
double_even_numbers(2) # 4
double_even_numbers(1) # 1
```
