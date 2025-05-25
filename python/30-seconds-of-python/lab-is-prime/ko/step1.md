# 숫자가 소수인지 확인

정수 `n`을 입력으로 받아 숫자가 소수이면 `True`를, 그렇지 않으면 `False`를 반환하는 Python 함수 `is_prime(n)`을 작성하십시오. 이 문제를 해결하려면 다음 규칙을 따라야 합니다.

- 숫자가 `0`, `1`, 음수 또는 `2`의 배수인 경우 `False`를 반환합니다.
- `all()`과 `range()`를 사용하여 `3`부터 주어진 숫자의 제곱근까지의 숫자를 확인합니다.
- 어떤 숫자도 주어진 숫자를 나누지 않으면 `True`를, 그렇지 않으면 `False`를 반환합니다.

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
