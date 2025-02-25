# 最大公約数

整数のリストを引数として受け取り、それらの最大公約数を返す `gcd(numbers)` という関数を書きます。あなたの関数は、与えられたリストに対して `functools.reduce()` と `math.gcd()` を使用する必要があります。

```python
from functools import reduce
from math import gcd as _gcd

def gcd(numbers):
  return reduce(_gcd, numbers)
```

```python
gcd([8, 36, 28]) # 4
```
