# 범위로 리스트 초기화

`initialize_list_with_range(end, start=0, step=1)` 함수를 작성하세요. 이 함수는 `start`와 `end`가 포함되고 공차 (common difference) 가 `step`인 지정된 범위 내의 숫자를 포함하는 리스트를 초기화합니다.

이 함수는 주어진 범위 내에서 원하는 값으로 채워진 적절한 길이의 리스트를 반환해야 합니다.

### 입력

- `end` (정수) - 범위의 끝 (포함).
- `start` (정수, 선택 사항) - 범위의 시작 (포함). 기본값은 0 입니다.
- `step` (정수, 선택 사항) - 범위 내 각 숫자 간의 공차. 기본값은 1 입니다.

### 출력

- 지정된 범위 내의 숫자를 포함하는 리스트.

```python
def initialize_list_with_range(end, start = 0, step = 1):
  return list(range(start, end + 1, step))
```

```python
initialize_list_with_range(5) # [0, 1, 2, 3, 4, 5]
initialize_list_with_range(7, 3) # [3, 4, 5, 6, 7]
initialize_list_with_range(9, 0, 2) # [0, 2, 4, 6, 8]
```
