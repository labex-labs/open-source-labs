# 기하 수열 (Geometric Progression)

`geometric_progression`이라는 함수를 작성하십시오. 이 함수는 세 개의 매개변수를 받습니다.

- `end`: 범위의 끝을 나타내는 정수 (포함)
- `start`: 범위의 시작을 나타내는 선택적 정수 (포함), 기본값은 `1`
- `step`: 두 항 사이의 공비 (common ratio) 를 나타내는 선택적 정수, 기본값은 `2`

이 함수는 두 항 사이의 비율이 `step`인 지정된 범위 내의 숫자들을 포함하는 리스트를 반환해야 합니다. 리스트는 `start`로 시작하여 `end`로 끝나야 합니다.

`step`이 `1`과 같으면 함수는 오류를 반환해야 합니다.

`range()`, `math.log()`, `math.floor()` 및 리스트 컴프리헨션 (list comprehension) 을 사용하여 각 요소에 `step`을 적용하여 적절한 길이의 리스트를 생성해야 합니다.

```python
from math import floor, log

def geometric_progression(end, start=1, step=2):
  return [start * step ** i for i in range(floor(log(end / start)
          / log(step)) + 1)]
```

```python
geometric_progression(256) # [1, 2, 4, 8, 16, 32, 64, 128, 256]
geometric_progression(256, 3) # [3, 6, 12, 24, 48, 96, 192]
geometric_progression(256, 1, 4) # [1, 4, 16, 64, 256]
```
