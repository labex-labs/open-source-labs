# 리스트 내 중복 확인 함수

`has_duplicates(lst)`라는 Python 함수를 작성하세요. 이 함수는 리스트를 인수로 받아 리스트에 중복된 요소가 있으면 `True`를 반환하고, 그렇지 않으면 `False`를 반환합니다.

이 문제를 해결하려면 다음 단계를 따를 수 있습니다.

1. 중복을 제거하기 위해 리스트를 set 으로 변환합니다.
2. set 의 길이와 원래 리스트의 길이를 비교합니다.
3. 길이가 같으면 리스트에 중복이 없고, 그렇지 않으면 중복이 있습니다.

```python
def all_unique(lst):
  return len(lst) == len(set(lst))
```

```python
x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 2, 3, 4, 5]
all_unique(x) # True
all_unique(y) # False
```
