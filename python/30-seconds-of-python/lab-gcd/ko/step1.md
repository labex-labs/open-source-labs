# 최대공약수 (Greatest Common Divisor)

정수 목록을 인수로 받아 최대공약수를 반환하는 `gcd(numbers)`라는 함수를 작성하십시오. 함수는 주어진 목록에 대해 `functools.reduce()`와 `math.gcd()`를 사용해야 합니다.

```python
from functools import reduce
from math import gcd as _gcd

def gcd(numbers):
  return reduce(_gcd, numbers)
```

```python
gcd([8, 36, 28]) # 4
```
