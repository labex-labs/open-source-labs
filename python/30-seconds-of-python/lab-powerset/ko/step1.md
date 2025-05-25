# 멱집합 (Powerset)

`powerset(iterable)`라는 Python 함수를 작성하세요. 이 함수는 iterable 을 인수로 받아 해당 iterable 의 멱집합을 반환합니다. 이 함수는 다음 단계를 따라야 합니다.

1. 주어진 값을 리스트로 변환합니다.
2. `range()`와 `itertools.combinations()`를 사용하여 모든 부분집합을 반환하는 제너레이터 (generator) 를 생성합니다.
3. `itertools.chain.from_iterable()`과 `list()`를 사용하여 제너레이터를 소비하고 리스트를 반환합니다.

```python
from itertools import chain, combinations

def powerset(iterable):
  s = list(iterable)
  return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
```

```python
powerset([1, 2]) # [(), (1,), (2,), (1, 2)]
```
