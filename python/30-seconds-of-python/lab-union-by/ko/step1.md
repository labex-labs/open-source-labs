# 함수 기반 리스트 합집합

두 리스트 `a`와 `b`와 함수 `fn`을 인자로 받는 함수 `union_by(a, b, fn)`을 작성하십시오. 이 함수는 두 리스트의 각 요소에 제공된 함수를 적용한 후, 두 리스트 중 하나라도 존재하는 모든 요소를 한 번씩 포함하는 리스트를 반환해야 합니다.

이 문제를 해결하려면 다음 단계를 따를 수 있습니다.

1. `a`의 각 요소에 `fn`을 적용하여 `set`을 생성합니다.
2. 리스트 컴프리헨션 (list comprehension) 을 `b`에 `fn`과 함께 사용하여 이전에 생성된 set, `_a`에 포함되지 않은 값만 유지합니다.
3. 마지막으로, 이전 결과와 `a`로부터 `set`을 생성하고 이를 `list`로 변환합니다.

이 함수는 다음과 같은 입력 매개변수를 가져야 합니다.

- `a`: 요소의 리스트
- `b`: 요소의 리스트
- `fn`: 요소를 받아 값을 반환하는 함수

이 함수는 요소의 리스트를 반환해야 합니다.

```python
def union_by(a, b, fn):
  _a = set(map(fn, a))
  return list(set(a + [item for item in b if fn(item) not in _a]))
```

```python
from math import floor

union_by([2.1], [1.2, 2.3], floor) # [2.1, 1.2]
```
