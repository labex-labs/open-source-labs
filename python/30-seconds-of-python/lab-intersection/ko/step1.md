# 리스트 교차 (List Intersection)

두 리스트 `a`와 `b`를 입력으로 받아 `a`와 `b` 모두에 존재하는 요소만 포함하는 새로운 리스트를 반환하는 함수 `list_intersection(a, b)`를 작성하십시오. 공통 요소가 없으면 함수는 빈 리스트를 반환해야 합니다.

```python
def intersection(a, b):
  _a, _b = set(a), set(b)
  return list(_a & _b)
```

```python
intersection([1, 2, 3], [4, 3, 2]) # [2, 3]
```
