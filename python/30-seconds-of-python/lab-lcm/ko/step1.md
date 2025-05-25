# 최소공배수 (Least Common Multiple)

숫자 목록을 인수로 받아 최소공배수를 반환하는 함수 `lcm(numbers)`를 작성하십시오. 함수는 두 숫자 `x`와 `y`의 LCM 을 계산하기 위해 다음 공식을 사용해야 합니다: `lcm(x, y) = x * y / gcd(x, y)`, 여기서 `gcd(x, y)`는 `x`와 `y`의 최대공약수 (greatest common divisor) 입니다.

이 문제를 해결하기 위해 `functools.reduce()` 함수를 사용하여 `lcm()` 공식을 목록의 모든 숫자에 적용할 수 있습니다. 또한 `math.gcd()` 함수를 사용하여 두 숫자의 최대공약수를 계산할 수 있습니다.

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
