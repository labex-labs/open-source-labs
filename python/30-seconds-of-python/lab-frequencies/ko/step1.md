# 값 빈도수

`value_frequencies(lst)`라는 Python 함수를 작성하세요. 이 함수는 리스트를 인수로 받아 리스트의 고유 값을 키로, 해당 빈도수를 값으로 하는 딕셔너리를 반환합니다.

이 문제를 해결하기 위해 다음 단계를 따를 수 있습니다.

1. 각 고유 요소의 빈도수를 저장할 빈 딕셔너리를 생성합니다.
2. 리스트를 반복하고 `collections.defaultdict`를 사용하여 각 고유 요소의 빈도수를 저장합니다.
3. `dict()`를 사용하여 리스트의 고유 요소를 키로, 해당 빈도수를 값으로 하는 딕셔너리를 반환합니다.

함수는 고유 값과 해당 빈도수를 포함하는 딕셔너리를 반환해야 합니다.

```python
from collections import defaultdict

def frequencies(lst):
  freq = defaultdict(int)
  for val in lst:
    freq[val] += 1
  return dict(freq)
```

```python
frequencies(['a', 'b', 'a', 'c', 'a', 'a', 'b']) # { 'a': 4, 'b': 2, 'c': 1 }
```
