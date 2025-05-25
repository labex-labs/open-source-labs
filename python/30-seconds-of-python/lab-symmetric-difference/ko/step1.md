# 대칭 차이 (Symmetric Difference)

두 리스트를 인수로 받아 그들의 대칭 차이를 리스트로 반환하는 함수 `symmetric_difference(a, b)`를 작성하십시오. 이 함수는 중복된 값을 필터링하지 않아야 합니다.

이 문제를 해결하기 위해 다음 단계를 따를 수 있습니다.

1. 각 리스트에서 집합 (set) 을 생성합니다.
2. 각 집합에 대해 리스트 컴프리헨션 (list comprehension) 을 사용하여 다른 집합에 포함되지 않은 값만 유지합니다.
3. 2 단계에서 얻은 두 리스트를 연결합니다.

```python
def symmetric_difference(a, b):
  (_a, _b) = (set(a), set(b))
  return [item for item in a if item not in _b] + [item for item in b
          if item not in _a]
```

```python
symmetric_difference([1, 2, 3], [1, 2, 4]) # [3, 4]
```
