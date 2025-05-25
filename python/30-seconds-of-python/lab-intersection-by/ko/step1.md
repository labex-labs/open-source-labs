# 함수 기반 리스트 교집합

두 개의 리스트 `a`와 `b`와 함수 `fn`을 입력으로 받는 함수 `intersection_by(a, b, fn)`을 작성하세요. 이 함수는 두 리스트의 각 요소에 제공된 함수를 적용한 후, 두 리스트 모두에 존재하는 요소들의 리스트를 반환해야 합니다.

### 입력

- 두 개의 리스트 `a`와 `b` (1 <= len(a), len(b) <= 1000)
- 하나의 인수를 받아 값을 반환하는 함수 `fn`

### 출력

- 두 리스트의 각 요소에 제공된 함수를 적용한 후, 두 리스트 모두에 존재하는 요소들의 리스트.

```python
def intersection_by(a, b, fn):
  _b = set(map(fn, b))
  return [item for item in a if fn(item) in _b]
```

```python
from math import floor

intersection_by([2.1, 1.2], [2.3, 3.4], floor) # [2.1]
```
