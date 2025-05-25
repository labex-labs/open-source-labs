# 부분합 리스트

숫자 리스트를 인수로 받아 부분합의 리스트를 반환하는 함수 `partial_sum(lst)`를 작성하십시오. 함수는 다음 단계를 수행해야 합니다.

1. `itertools.accumulate()`를 사용하여 리스트의 각 요소에 대한 누적 합을 생성합니다.
2. `list()`를 사용하여 결과를 리스트로 변환합니다.
3. 부분합의 리스트를 반환합니다.

```python
from itertools import accumulate

def cumsum(lst):
  return list(accumulate(lst))
```

```python
cumsum(range(0, 15, 3)) # [0, 3, 9, 18, 30]
```
