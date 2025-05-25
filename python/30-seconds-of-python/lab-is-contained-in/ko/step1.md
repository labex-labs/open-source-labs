# 리스트 포함 여부 (List Containment)

두 개의 리스트를 인수로 받아 리스트 `a`의 모든 요소가 리스트 `b`에 포함되어 있는지 여부를 순서에 관계없이 확인하고 `True`를 반환하는 함수 `is_contained_in(a, b)`를 작성하십시오. 그렇지 않으면 함수는 `False`를 반환해야 합니다.

이 문제를 해결하기 위해 다음 접근 방식을 사용할 수 있습니다.

1. 리스트 `a`의 각 고유 값에 대해 반복합니다.
2. 각 값에 대해, 해당 값이 리스트 `a`에서 리스트 `b`보다 더 많이 나타나는지 확인합니다.
3. 어떤 값이 리스트 `a`에서 리스트 `b`보다 더 많이 나타나면 `False`를 반환합니다.
4. 리스트 `a`의 모든 값이 리스트 `a`에서 나타나는 횟수 이상으로 리스트 `b`에 나타나면 `True`를 반환합니다.

```python
def is_contained_in(a, b):
  for v in set(a):
    if a.count(v) > b.count(v):
      return False
  return True
```

```python
is_contained_in([1, 4], [2, 4, 1]) # True
```
