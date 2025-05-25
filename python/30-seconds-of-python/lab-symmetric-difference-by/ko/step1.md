# 함수 기반 대칭 차이 (Symmetric Difference Based on Function)

두 리스트 `a`와 `b`와 함수 `fn`을 인수로 받는 함수 `symmetric_difference_by(a, b, fn)`을 작성하십시오. 이 함수는 두 리스트의 각 요소에 제공된 함수를 적용한 후 원래 리스트 중 하나에는 있지만 둘 다에는 없는 모든 요소를 포함하는 새로운 리스트를 반환해야 합니다.

이 문제를 해결하려면 다음 단계를 따를 수 있습니다.

1. 각 리스트의 각 요소에 `fn`을 적용하여 `set`을 생성합니다.
2. 각 리스트에 대해 `fn`과 함께 리스트 컴프리헨션 (list comprehension) 을 사용하여 다른 리스트에서 생성된 set 에 포함되지 않은 값만 유지합니다.
3. 2 단계에서 얻은 두 리스트를 연결합니다.

이 함수는 다음과 같은 매개변수를 가져야 합니다.

- `a`: 요소의 리스트
- `b`: 요소의 리스트
- `fn`: 요소를 받아 새로운 값을 반환하는 함수

이 함수는 두 리스트의 각 요소에 제공된 함수를 적용한 후 원래 리스트 중 하나에는 있지만 둘 다에는 없는 모든 요소를 포함하는 새로운 리스트를 반환해야 합니다.

```python
def symmetric_difference_by(a, b, fn):
  (_a, _b) = (set(map(fn, a)), set(map(fn, b)))
  return [item for item in a if fn(item) not in _b] + [item
          for item in b if fn(item) not in _a]
```

```python
from math import floor

symmetric_difference_by([2.1, 1.2], [2.3, 3.4], floor) # [1.2, 3.4]
```
