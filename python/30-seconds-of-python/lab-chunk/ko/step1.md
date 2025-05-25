# 리스트를 청크로 분할하기

리스트 `lst`와 양의 정수 `size`를 인수로 받아 각 최대 크기가 `size`인 더 작은 리스트의 리스트를 반환하는 함수 `chunk(lst, size)`를 작성하십시오. `lst`의 길이가 `size`로 균등하게 나누어지지 않으면 반환된 리스트의 마지막 리스트는 나머지 요소를 포함해야 합니다.

```python
from math import ceil

def chunk(lst, size):
  return list(
    map(lambda x: lst[x * size:x * size + size],
      list(range(ceil(len(lst) / size)))))
```

```python
chunk([1, 2, 3, 4, 5], 2) # [[1, 2], [3, 4], [5]]
```
