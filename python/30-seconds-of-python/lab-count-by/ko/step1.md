# 그룹화된 요소 개수 세기

리스트 `lst`와 함수 `fn`을 인수로 사용하는 함수 `count_by(lst, fn = lambda x: x)`를 작성하십시오. 이 함수는 주어진 함수를 기반으로 리스트의 요소를 그룹화하고 각 그룹의 요소 수를 포함하는 딕셔너리를 반환해야 합니다.

이 문제를 해결하려면 다음 단계를 따를 수 있습니다.

1. `collections.defaultdict`를 사용하여 딕셔너리를 초기화합니다.
2. `map()`을 사용하여 주어진 함수를 리스트의 각 요소에 적용합니다.
3. 매핑된 값을 반복하고 딕셔너리에서 각 요소의 개수를 증가시킵니다.

함수는 결과 딕셔너리를 반환해야 합니다.

```python
from collections import defaultdict

def count_by(lst, fn = lambda x: x):
  count = defaultdict(int)
  for val in map(fn, lst):
    count[val] += 1
  return dict(count)
```

```python
from math import floor

count_by([6.1, 4.2, 6.3], floor) # {6: 2, 4: 1}
count_by(['one', 'two', 'three'], len) # {3: 2, 5: 1}
```
