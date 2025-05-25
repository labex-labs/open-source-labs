# 패리티 이상치 찾기

정수 리스트 `nums`를 인자로 받아 `nums` 내의 모든 패리티 이상치를 리스트로 반환하는 함수 `find_parity_outliers(nums)`를 작성하세요.

이 문제를 해결하기 위해 다음 단계를 따를 수 있습니다.

1. 리스트 컴프리헨션 (list comprehension) 과 함께 `collections.Counter`를 사용하여 리스트 내의 짝수 및 홀수 값을 셉니다.
2. `collections.Counter.most_common()`을 사용하여 가장 흔한 패리티를 얻습니다.
3. 리스트 컴프리헨션을 사용하여 가장 흔한 패리티와 일치하지 않는 모든 요소를 찾습니다.

```python
from collections import Counter

def find_parity_outliers(nums):
  return [
    x for x in nums
    if x % 2 != Counter([n % 2 for n in nums]).most_common()[0][0]
  ]
```

```python
find_parity_outliers([1, 2, 3, 4, 6]) # [1, 3]
```
