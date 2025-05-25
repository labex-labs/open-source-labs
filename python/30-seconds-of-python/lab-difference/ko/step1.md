# 리스트 차이 (List Difference)

두 개의 리스트를 인수로 받아 그 차이를 반환하는 Python 함수 `list_difference(a, b)`를 작성하십시오. 이 함수는 중복 값을 필터링하지 않아야 합니다. 이 문제를 해결하려면 다음 단계를 따를 수 있습니다.

1. 두 번째 리스트 `b`에서 set 을 생성합니다.
2. 첫 번째 리스트 `a`에 대해 리스트 컴프리헨션 (list comprehension) 을 사용하여 이전에 생성된 set `_b`에 포함되지 않은 값만 유지합니다.
3. 결과 리스트를 반환합니다.

```python
def difference(a, b):
  _b = set(b)
  return [item for item in a if item not in _b]
```

```python
difference([1, 2, 3], [1, 2, 4]) # [3]
```
