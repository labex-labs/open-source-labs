# 最小公倍数

引数として数値のリストを受け取り、それらの最小公倍数を返す関数`lcm(numbers)`を書きます。関数は、2つの数`x`と`y`の最小公倍数を計算するために次の式を使用する必要があります。`lcm(x, y) = x * y / gcd(x, y)`。ここで、`gcd(x, y)`は`x`と`y`の最大公約数です。

この問題を解くには、`functools.reduce()`関数を使用して、リスト内のすべての数に`lcm()`の式を適用することができます。また、2つの数の最大公約数を計算するために`math.gcd()`関数を使用することもできます。

```python
from functools import reduce
from math import gcd

def lcm(numbers):
  return reduce((lambda x, y: int(x * y / gcd(x, y))), numbers)
```

```python
lcm([12, 7]) # 84
lcm([1, 3, 4, 5]) # 60
```
