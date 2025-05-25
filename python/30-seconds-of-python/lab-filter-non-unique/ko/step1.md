# 중복되지 않는 리스트 값 필터링

`filter_non_unique(lst)`라는 Python 함수를 작성하세요. 이 함수는 리스트를 인수로 받아 고유한 값만 포함하는 새로운 리스트를 반환합니다. 이 문제를 해결하려면 다음 단계를 따르세요.

1. `collections.Counter` 메서드를 사용하여 리스트의 각 값의 개수를 구합니다.
2. 리스트 컴프리헨션 (list comprehension) 을 사용하여 고유한 값만 포함하는 리스트를 생성합니다.

```python
from collections import Counter

def filter_non_unique(lst):
  return [item for item, count in Counter(lst).items() if count == 1]
```

```python
filter_non_unique([1, 2, 2, 3, 4, 4, 5]) # [1, 3, 5]
```
