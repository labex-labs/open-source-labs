# 리스트를 N 개의 청크로 분할하기

`lst`라는 리스트와 정수 `n`을 입력으로 받아 원래 리스트의 요소를 동일한 수로 포함하는 `n`개의 더 작은 리스트의 리스트를 반환하는 Python 함수 `chunk_into_n(lst, n)`을 작성하십시오. 원래 리스트를 `n`개의 더 작은 리스트로 균등하게 분할할 수 없는 경우, 마지막 청크에는 나머지 요소가 포함되어야 합니다.

이 문제를 해결하려면 다음 단계를 따를 수 있습니다.

1. 원래 리스트의 길이를 `n`으로 나누고 `math.ceil()` 함수를 사용하여 가장 가까운 정수로 올림하여 각 청크의 크기를 계산합니다.
2. `list()` 및 `range()` 함수를 사용하여 크기가 `n`인 새 리스트를 생성합니다.
3. `map()` 함수를 사용하여 새 리스트의 각 요소를 `size` 길이의 원래 리스트의 청크에 매핑합니다.
4. 더 작은 리스트의 리스트를 반환합니다.

함수는 다음과 같은 시그니처 (signature) 를 가져야 합니다.

```python
def chunk_into_n(lst: list, n: int) -> list:
```

```python
from math import ceil

def chunk_into_n(lst, n):
  size = ceil(len(lst) / n)
  return list(
    map(lambda x: lst[x * size:x * size + size],
    list(range(n)))
  )
```

```python
chunk_into_n([1, 2, 3, 4, 5, 6, 7], 4) # [[1, 2], [3, 4], [5, 6], [7]]
```
