# 純粋な Python 関数の実装

まずは、DataFrame に対して行ごとに操作を行う純粋な Python 関数を作成します。

```python
# 関数を定義
def f(x):
    return x * (x - 1)

# 最初の関数を使用する別の関数を定義
def integrate_f(a, b, N):
       s = 0
       dx = (b - a) / N
       for i in range(N):
           s += f(a + i * dx)
       return s * dx
```
