# 리스트 요소 오프셋 (Offset)

리스트 `lst`와 정수 `offset`을 인수로 받아 지정된 수의 요소를 리스트의 끝으로 이동시킨 새로운 리스트를 반환하는 함수 `offset(lst, offset)`를 작성하십시오. `offset`이 양수이면 처음 `offset`개의 요소를 리스트의 끝으로 이동합니다. `offset`이 음수이면 마지막 `offset`개의 요소를 리스트의 시작 부분으로 이동합니다.

```python
def offset(lst, offset):
  return lst[offset:] + lst[:offset]
```

```python
offset([1, 2, 3, 4, 5], 2) # [3, 4, 5, 1, 2]
offset([1, 2, 3, 4, 5], -2) # [4, 5, 1, 2, 3]
```
