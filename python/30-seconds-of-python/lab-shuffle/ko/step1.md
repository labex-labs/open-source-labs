# 리스트 섞기 (Shuffle List)

입력으로 리스트를 받아 무작위 순서로 동일한 항목들을 포함하는 새로운 리스트를 반환하는 함수 `shuffle(lst)`를 작성하십시오. 함수는 리스트 내 항목들을 섞기 위해 Fisher-Yates 알고리즘을 사용해야 합니다.

Fisher-Yates 알고리즘은 다음과 같이 작동합니다.

1. 리스트의 마지막 항목부터 시작합니다.
2. 0 과 현재 인덱스 사이의 임의의 인덱스를 생성합니다.
3. 현재 인덱스의 항목을 임의의 인덱스의 항목과 교환합니다.
4. 리스트의 다음 항목으로 이동하여 모든 항목이 섞일 때까지 2-3 단계를 반복합니다.

함수는 원래 리스트를 수정해서는 안 됩니다. 대신, 섞인 항목들을 포함하는 새로운 리스트를 생성해야 합니다.

입력 리스트에는 최소한 하나의 항목이 포함되어 있다고 가정할 수 있습니다.

```python
from copy import deepcopy
from random import randint

def shuffle(lst):
  temp_lst = deepcopy(lst)
  m = len(temp_lst)
  while (m):
    m -= 1
    i = randint(0, m)
    temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
  return temp_lst
```

```python
foo = [1, 2, 3]
shuffle(foo) # [2, 3, 1], foo = [1, 2, 3]
```
