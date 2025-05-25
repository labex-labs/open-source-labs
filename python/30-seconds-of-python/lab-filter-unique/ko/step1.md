# 고유하지 않은 리스트 값 필터링

`filter_unique(lst)`라는 Python 함수를 작성하세요. 이 함수는 리스트를 인수로 받아 고유하지 않은 값들만 포함하는 새로운 리스트를 반환합니다. 이 문제를 해결하기 위해 다음 단계를 따를 수 있습니다.

1. `collections.Counter`를 사용하여 리스트의 각 값의 개수를 구합니다.
2. 리스트 컴프리헨션 (list comprehension) 을 사용하여 고유하지 않은 값들만 포함하는 리스트를 생성합니다.

함수는 다음 요구 사항을 충족해야 합니다.

- 함수는 리스트를 인수로 받아야 합니다.
- 함수는 고유하지 않은 값들만 포함하는 새로운 리스트를 반환해야 합니다.
- 함수는 원래 리스트를 수정해서는 안 됩니다.
- 함수는 대소문자를 구분해야 합니다. 즉, 'a'와 'A'는 서로 다른 값으로 간주됩니다.

```python
def filter_unique(lst):
    # your code here
```

```python
from collections import Counter

def filter_unique(lst):
  return [item for item, count in Counter(lst).items() if count > 1]
```

```python
filter_unique([1, 2, 2, 3, 4, 4, 5]) # [2, 4]
```
