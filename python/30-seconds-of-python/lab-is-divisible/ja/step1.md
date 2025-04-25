# 数は割り切れる

2 つの整数を引数として受け取り、`dividend` が `divisor` で割り切れる場合は `True` を返し、そうでない場合は `False` を返す関数 `is_divisible(dividend, divisor)` を作成します。

```python
def is_divisible(dividend, divisor):
  return dividend % divisor == 0
```

```python
is_divisible(6, 3) # True
```
