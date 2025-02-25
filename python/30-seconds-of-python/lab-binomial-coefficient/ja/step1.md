# 二項係数

2つの整数 `n` と `k` を引数にとり、`n` と `k` の二項係数を返す `binomial_coefficient(n, k)` という関数を作成します。この関数は、二項係数を計算するために `math.comb()` メソッドを使用する必要があります。

```python
from math import comb

def binomial_coefficient(n, k):
  return comb(n, k)
```

```python
binomial_coefficient(8, 2) # 28
```
