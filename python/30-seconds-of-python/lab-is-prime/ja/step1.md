# 数が素数であるかどうか

整数 `n` を入力として受け取り、その数が素数であれば `True` を返し、そうでなければ `False` を返す Python 関数 `is_prime(n)` を書きます。この問題を解くには、次のルールに従う必要があります。

- 数が 0、1、負の数または 2 の倍数の場合、`False` を返します。
- `all()` と `range()` を使って、3 から与えられた数の平方根までの数をチェックします。
- もしどの数も与えられた数を割り切らなければ `True` を返し、そうでなければ `False` を返します。

```python
from math import sqrt

def is_prime(n):
  if n <= 1 or (n % 2 == 0 and n > 2):
    return False
  return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))
```

```python
is_prime(11) # True
```
