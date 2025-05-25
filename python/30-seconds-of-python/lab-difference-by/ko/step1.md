# 함수 기반 리스트 차이

`difference_by(a, b, fn)`이라는 함수를 만드세요. 이 함수는 세 개의 매개변수를 받습니다.

- `a`: 요소의 리스트
- `b`: 요소의 리스트
- `fn`: 두 리스트의 각 요소에 적용될 함수

이 함수는 두 리스트의 각 요소에 제공된 함수 `fn`을 적용한 후, 리스트 `a`에는 있지만 리스트 `b`에는 없는 요소의 리스트를 반환해야 합니다.

이 문제를 해결하려면 다음 단계를 따르세요.

1. `map()`을 사용하여 `b`의 각 요소에 `fn`을 적용하여 `set`을 생성합니다.
2. 리스트 컴프리헨션 (list comprehension) 을 `a`에 있는 `fn`과 함께 사용하여 이전에 생성된 set `_b`에 포함되지 않은 값만 유지합니다.

```python
def difference_by(a, b, fn):
  _b = set(map(fn, b))
  return [item for item in a if fn(item) not in _b]
```

```python
from math import floor

difference_by([2.1, 1.2], [2.3, 3.4], floor) # [1.2]
difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x'])
# [ { x: 2 } ]
```
