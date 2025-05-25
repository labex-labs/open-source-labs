# 이항 계수 (Binomial Coefficient)

두 정수 `n`과 `k`를 입력으로 받아 `n`과 `k`의 이항 계수를 반환하는 `binomial_coefficient(n, k)`라는 함수를 작성하십시오. 함수는 `math.comb()` 메서드를 사용하여 이항 계수를 계산해야 합니다.

```python
from math import comb

def binomial_coefficient(n, k):
  return comb(n, k)
```

```python
binomial_coefficient(8, 2) # 28
```
